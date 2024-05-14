from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('events/', views.events, name='events'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services_list, name='services_list'),
    path('blog/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('programs/', views.programs_list, name='programs_list'),
]
