from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .forms import UserProfileForm

def home_pag(request):

    return render(request,'home/homes.html')


def nuse_pag(request):

    return render(request,'home/nuse.html')


def lockhome_pag(request):

    return render(request,'home/lockhome.html')

#regstru


def sing_pag(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('log')  
    else:
        form = UserRegistrationForm()

    return render(request,'conta/sing.html', {'form': form})


def log_pag(request):
    login_form = CustomLoginForm()
    if request.method == 'POST':
        login_form = CustomLoginForm(data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('lockhome')
        else:
            login_form = CustomLoginForm()

    return render(request,'conta/log.html',{'login_form': login_form})

def user_logout(request):
    logout(request)
    return redirect('home')

#####

def profil_pag(request):
    user_info = Profile.objects.get(user=request.user)
    context ={
        'user_info':user_info
    }
    return render(request,'home/profil.html',context)


def profil_updt(request):
    info = Profile.objects.get(user=request.user)
    form = UserProfileForm(instance=info)
    if request.method == 'POST':
        form =UserProfileForm(request.POST, request.FILES,instance=info)
        if form.is_valid():
            form.save()
            return redirect('prof') 
    else:
        form = UserProfileForm()
    context ={
        'info':form
    }
    return render(request,'home/updet.html',context)


def profil_updt_to(request):
    info = Profile.objects.get(user=request.user)
    form = UserProfileForm(instance=info)
    if request.method == 'POST':
       form = UserProfileForm(request.POST,request.FILES,instance=info)
    if form.is_valid():
       form.save()
       return redirect('prof') 
    context ={
        'info':form
    }
    return render(request,'home/updet_to.html',context)