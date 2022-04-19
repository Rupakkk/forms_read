
from re import template
from django.shortcuts import render
from django.views.generic import CreateView,ListView,TemplateView
from app.models import FormModel


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'




class HomeView(CreateView):
    model = FormModel
    success_url = 'post'
    fields = '__all__'
    template_name = 'accounts/login.html'
   
class PostView(ListView):
    model = FormModel
    template_name = 'registration/profile.html'
    context_object_name = 'forms'
    


