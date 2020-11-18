from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home,name='user_home'),
    url(r'^logout/', views.logout_view, name='logout'),
    path('image_table/', views.Image_Table, name='image_table'),
    path('image_galery/', views.image_galery, name='image_galery'),
    path('quiz_micro/', views.quiz_micro, name='quiz_micro'),
    path('quiz_component/', views.quiz_component, name='quiz_component')
]
