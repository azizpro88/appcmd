from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
  path('', views.index,name='index'),
 # path('<int:id>', views.detail_page,name='detail'),
  path('admin/', views.admin,name='admin'),
]