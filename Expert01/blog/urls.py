from django.contrib import admin
from . import views  # 해당 디렉토리 내 view 내용 가져오라는 뜻
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index)   # views 파일의 index란 함수를 찾아서 처리하란 뜻
]