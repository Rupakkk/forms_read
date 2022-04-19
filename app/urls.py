from django.urls import path
from app import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('post/',views.PostView.as_view(),name="post")
]
