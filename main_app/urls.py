from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name ='home'),
    path('about/', views.About.as_view(), name='about'),
    path('finches/', views.FinchList.as_view(), name='finches'),
    path('finch/new/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/', views.FinchDetail.as_view(), name='finch_detail'),
    path('finch/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:pk>/cars/new', views.CarCreate.as_view(), name='car_create'),
    path('bodys/<int:pk>/cars/<int:car_pk>/', views.BodyCarAssoc.as_view(), name='body_car_assoc'),
]