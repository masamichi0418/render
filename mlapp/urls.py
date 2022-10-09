from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_form, name='input_form'),
    path('input_form/', views.input_form, name='input_form'),
    path('result/', views.result, name='result'), # 追加
]