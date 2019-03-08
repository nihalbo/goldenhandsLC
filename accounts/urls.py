from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
app_name = "users"

urlpatterns = [
    url(r'^$', views.home),
    url('aboutus/', views.aboutus),
    url('opportunities/', views.opportunities),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile')

]

#from django.contrib.auth import views
#url('login/', views.LoginView.as_view('template_name'=='accounts/login.html'),name='login'),
