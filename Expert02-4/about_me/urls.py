from . import views
from django.urls import path, include

urlpatterns = [
    path('about_me/', views.about_me),
    path('',views.landing)
]