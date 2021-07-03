from . import views  #해당 디렉토리 내 view 내용 가져오라는 뜻
from django.urls import path, include

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing), # 아무것도 없으면 landing 찾으란뜻
]