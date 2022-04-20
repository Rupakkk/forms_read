from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,TemplateView
from app.models import FormModel
from .forms import SignUpForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class =SignUpForm
    success_url = 'post'
    template_name = 'register.html'

class HomeView(CreateView):
    model = FormModel
    success_url = 'post'
    fields = '__all__'
    template_name = 'accounts/login.html'
   
class PostView(ListView):
    model = FormModel
    template_name = 'registration/profile.html'
    context_object_name = 'forms'
    


