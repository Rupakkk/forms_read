from django.urls import path
from app import views
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('',views.HomeView.as_view(),name='home'),
    path('profile/',views.PostView.as_view(),name="post")
]
