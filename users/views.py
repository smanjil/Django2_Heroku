# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.urls import (
    reverse, 
    reverse_lazy
)
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, 
    login,
    logout
)

from users.forms import (
    RegisterForm,
    LoginForm,
    ResetPasswordForm
)

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        messages.add_message(
            self.request, 
            messages.SUCCESS, 
            'You have successfully registered your account!'
        )
        return reverse('users:login')

class LoginView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'users/login.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        username = form.data['username']
        password = form.data['password']

        user = authenticate(
            request, 
            username = username, 
            password = password
        )

        if user is not None:
            login(request, user)
            messages.add_message(
                self.request, 
                messages.SUCCESS, 
                'You have successfully logged in!'
            )
            return HttpResponseRedirect('/genericviews/')
        else:
            messages.add_message(
                self.request, 
                messages.ERROR, 
                'Oops! Login Error'
            )
            return HttpResponseRedirect('/users/login')

def logout_user(request):
    messages.add_message(
        request, 
        messages.SUCCESS, 
        'You have successfully logged out!'
    )
    logout(request)
    return HttpResponseRedirect('/users/login')

class ResetPasswordView(FormView):
    model = User
    form_class = ResetPasswordForm
    template_name = 'users/password_reset.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        username = form.data['username']
        password = form.data['password']

        try:
            user = User.objects.all().filter(username = username)[0]
            user.set_password(password)
            user.save()

            messages.add_message(
                self.request, 
                messages.SUCCESS, 
                'You have successfully changed your password!'
            )
            return HttpResponseRedirect('/users/login')
        except:
            messages.add_message(
                self.request, 
                messages.ERROR, 
                'Oops! This user does not exist!'
            )
            return HttpResponseRedirect('/users/reset')