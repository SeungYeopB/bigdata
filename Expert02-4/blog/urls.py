from . import views
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
#    path('<int:pk>/', views.single_post_page),
#    path('', views.index)
]