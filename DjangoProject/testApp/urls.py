from django.urls import path
from testApp import views

app_name = "testApp"

urlpatterns = [
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('post/',views.sample_post, name="post")
]