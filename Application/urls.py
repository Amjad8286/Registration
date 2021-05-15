from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('report/', views.report, name='report'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('submit/', views.submit, name='submit'),
    path('handle_logout/', views.logout, name='logout')
]
