from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import App
from django.urls import reverse
# Create your views here.
def index2(request):
    mymembers=App.objects.all().values()
    template=loader.get_template('file1.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))
def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=App(first_name=x,last_name=y)
    member.save()
    return HttpResponseRedirect(reverse('index2'))
def delete(request,id):
    new=App.objects.get(id=id)
    new.delete()
    return HttpResponseRedirect(reverse('index2'))
def update(request,id):
    mymember=App.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))
def updaterecord(request,id):
    first=request.POST['first']
    last=request.POST['last']
    member=App.objects.get(id=id)
    member.first_name=first
    member.last_name=last
    member.save()
    return HttpResponseRedirect(reverse('index2'))