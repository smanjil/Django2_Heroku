# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (
    render,
    HttpResponseRedirect, 
    reverse
)
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

from genericviews.forms import ProductForm
from genericviews.models import Product

class CreateProductView(LoginRequiredMixin, generic.FormView):
    model = Product
    form_class = ProductForm
    template_name = 'genericviews/makeentry.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, 'genericviews/makeentry.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        title = form.data['title']
        desc = form.data['desc']

        Product.objects.create(
            user = request.user, 
            title = title, 
            desc = desc
        )

        form = ProductForm()

        messages.add_message(
            request, 
            messages.SUCCESS, 
            'You have successfully created a product!'
        )
        return HttpResponseRedirect('/genericviews/')

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'genericviews/index.html'
    paginate_by = 2

    login_url = '/users/login'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Product.objects.all().filter(user = self.request.user).order_by('id')

    def get_paginate_by(self, queryset):
        if 'paginate_by' in self.request.GET:
            self.request.session['paginate_by'] = self.request.GET['paginate_by']
            self.paginate_by = self.request.session.get('paginate_by', self.paginate_by)
        elif 'page' in self.request.GET:
            self.paginate_by = self.request.session.get('paginate_by', self.paginate_by)
        else:
            if 'paginate_by' in self.request.session:
                del self.request.session['paginate_by']
        
        return self.paginate_by

class DetailsView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'genericviews/detail.html'

    login_url = '/users/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(DetailsView, self).get_context_data(**kwargs)

        context['new_list'] = Product.objects.all().filter(~Q(user = self.request.user)).order_by('id')

        return context

class EditView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['title', 'desc']
    template_name_suffix = '_update_form'

    login_url = '/users/login'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        messages.add_message(
            self.request, 
            messages.SUCCESS, 
            'You have successfully update the product!'
        )
        return reverse('genericviews:detail', kwargs = {'pk': self.kwargs['pk']})

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product

    login_url = '/users/login'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        messages.add_message(
            self.request, 
            messages.SUCCESS, 
            'You have successfully deleted a product!'
        )
        return reverse('genericviews:index')