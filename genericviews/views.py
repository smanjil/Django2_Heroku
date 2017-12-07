# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import generic
from django.contrib import messages

# Create your views here.

from genericviews.forms import ProductForm
from genericviews.models import Product


def makeentry(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            title = request.POST.get('title', '')
            desc = request.POST.get('desc', '')

        product = Product(title = title, desc = desc)
        product.save()

        form = ProductForm()

        messages.add_message(request, messages.SUCCESS, 'redirect')
        return HttpResponseRedirect('/genericviews/')
    else:
        form = ProductForm()
        return render(request, 'genericviews/makeentry.html', {'form': form})

class IndexView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'genericviews/index.html'
    paginate_by = 2
    queryset = Product.objects.all()

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

class DetailsView(generic.DetailView):
    model = Product
    template_name = 'genericviews/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailsView, self).get_context_data(**kwargs)

        context['new_list'] = Product.objects.all()

        return context

class EditView(generic.UpdateView):
    model = Product
    fields = ['title', 'desc']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'redirect')
        return reverse('genericviews:detail', kwargs = {'pk': self.kwargs['pk']})

class DeleteView(generic.DeleteView):
    model = Product

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'redirect')
        return reverse('genericviews:index')