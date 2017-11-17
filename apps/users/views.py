# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from .models import User
# Create your views here.
def index(req):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(req, 'users/users.html', context)

def new(req):
    return render(req, 'users/new.html')

def create(req):
    User.objects.create(first_name=req.POST['fname'], last_name= req.POST['lname'], email_id = req.POST['email'])    
    return redirect('/users')

def edit(req, id):
    return render(req, 'users/edit.html', {"user": User.objects.get(id = id)})

def update(req):
    errors = User.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
            return redirect('/users/'+req.POST['userid']+'/edit')
    else:
        user = User.objects.get(id = req.POST['userid'])
        user.first_name = req.POST['fname']
        user.last_name = req.POST['lname']
        user.email_id = req.POST['email']
        user.save()
        return redirect('/users')

def show(req, id):
    return render(req, 'users/show.html', {"user": User.objects.get(id = id)})

def delete(req, id):
    User.objects.get(id = id).delete()
    return redirect('/users')