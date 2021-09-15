from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *

# Create your views here.
def registration(request):
    if request.method=='POST':
        m=registerform(request.POST)
        if m.is_valid():
            name = m.cleaned_data['n_ame']
            email = m.cleaned_data['e_mail']
            mobile = m.cleaned_data['m_obile']
            address = m.cleaned_data['a_ddress']
            #gender = m.cleaned_data['g_ender']
            pwd = m.cleaned_data['p_wd']
            n = registermodel(n_ame=name, e_mail=email, m_obile=mobile, a_ddress=address,  p_wd=pwd)
            n.save()
            return redirect('/app/login/')
        else:
            return HttpResponse('Error')
    else:
        return render(request,"studentregister.html")

def login(request):
    if request.method=='POST':
        m=loginform(request.POST)
        if m.is_valid():
            email=m.cleaned_data['e_mail']
            pwd=m.cleaned_data['p_wd']
            c=registermodel.objects.all()
            for i in c:
                if email==i.e_mail and pwd==i.p_wd:
                    return redirect('/app/update/')
        else:
            return HttpResponse('Invalid email id or password')
    else:
        return render(request,"login.html")

def updation(request):
    if request.method=="POST":
        m=updateform(request.POST,request.FILES)
        if m.is_valid():
            name = m.cleaned_data['n_ame']
            photo = m.cleaned_data['p_hoto']
            mobile = m.cleaned_data['m_obile']
            address = m.cleaned_data['a_ddress']
            b = updatemodel(p_hoto = photo, n_ame=name, m_obile=mobile, a_ddress=address)
            b.save()
            return HttpResponse('Profile Updated successfully')
        else:
            return HttpResponse('Error')
    else:
        return render(request,'update.html')

def about(request):
    return render(request,"index.html")
