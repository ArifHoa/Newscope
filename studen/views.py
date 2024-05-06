from django.shortcuts import render, redirect
from .models import Casterm
from .forms import CastermForm


def veo(request):
    casterms = Casterm.objects.all()
    context ={
        'casterms':casterms
    }
    return render(request,'cord/craet.html',context)


def add_casterm(request):
    if request.method == 'POST':
        form = CastermForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prof') 
    else:
        form = CastermForm()
    context ={
        'form':form
    }    
    return render(request, 'cord/crct.html',context)





def updete_vew(request,pk):
    upde = Casterm.objects.get(id=pk)
    form = CastermForm(instance=upde)
    if request.method == 'POST':
        form = CastermForm(request.POST,request.FILES,instance=upde)
        form.save()
        return redirect('veo') 
    context ={
        'form':form
    } 
    return render(request,'cord/updet.html',context)
