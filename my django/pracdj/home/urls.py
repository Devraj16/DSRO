
from django.contrib import admin
from django.urls import path, include
from home import views
# from home.views import login_view

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("blog", views.blog, name='blog'),
    path("contact", views.contact, name='contact'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('dyson', views.dyson, name='dyson'),
    path('voidwalker', views.voidwalker, name='voidwalker'),
    path('kepler', views.kepler, name='kepler'),
    path('intergalactic', views.intergalactic, name='intergalactic'),
    path('quantum', views.quantum, name='quantum'),
    path('terraforming', views.terraforming, name='terraforming'),
    # path('',include('home.urls')),

    
]