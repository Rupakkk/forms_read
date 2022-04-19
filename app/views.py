
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from app.models import FormModel


# Create your views here.
class HomeView(CreateView):
    model = FormModel
    success_url = 'post'
    fields = '__all__'
    template_name = 'index.html'
   
class PostView(ListView):
    model = FormModel
    template_name = 'post.html'
    context_object_name = 'forms'
    


