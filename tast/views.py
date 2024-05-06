from django.shortcuts import render, redirect
from hom.models import Profile
from hom.forms import UserProfileForm





def tex(request):
    info = Profile.objects.get(user=request.user)
    form = UserProfileForm(instance=info)
    if request.method == 'POST':
       form = UserProfileForm(request.POST,request.FILES,instance=info)
    if form.is_valid():
       form.save()
    context ={
        'info':form
    }
    return render(request,'testme/ttxx.html',context)