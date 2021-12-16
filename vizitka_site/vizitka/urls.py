from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('our-works', views.works, name='works'),
    path('call', views.to_call, name='call'),
    path('thanks', views.thanks, name='thanks')
]
