# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import generic
from .models import Content
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import datetime    
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm, PasswordForm

class ContentListView(generic.ListView):
    model = Content
    ordering = ['-id']   
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
    model = User
    ordering = ['-id']       
    
class ContentDetailView(generic.DetailView):
    model = Content
    
class ContentCreate(CreateView):
    model = Content
    fields = ['subject', 'description', 'reporter', 'phone', 'picture']
    success_url = "/"   
    template_name = 'form.html'   
    
class UserCreate(CreateView):
    model = User
    form_class = UserForm
    success_url = "/web/user/"   
    template_name = 'form.html'    
      
@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = User
    form_class = UserForm    
    success_url = "/web/user/"   
    template_name = 'form.html'   
    
@method_decorator(login_required, name='dispatch')
class PasswordUpdate(UpdateView):
    model = User
    form_class = PasswordForm    
    success_url = "/web/user/"   
    template_name = 'form.html' 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        return super().form_valid(form)  
      
    def get_initial(self):
        data = {}
        data['password'] = ""
        return data      
    
@method_decorator(login_required, name='dispatch')
class ContentUpdate(UpdateView):
    model = Content
    fields = ['handler', 'status', 'comment', 'handle_date']
    success_url = "/"   
    template_name = 'web/content_form.html'
    
    def get_initial(self):
        data = {}
        if self.request.user.first_name:
          data['handler'] = self.request.user.first_name
        else:
          data['handler'] = self.request.user.username
        data['handle_date'] = datetime.now
        return data