from django.urls import path
from mysite import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact",views.contact, name='contact'),
    path("signup",views.signup, name='signup'),
    path("login", views.signin,name='login'),
    path('home',views.home, name='home'),
    path('logout',views.logoutuser, name='logout'),
    path('about',views.dashboard, name='about'),
    path('inner',views.dashboard_inner, name='inner'),
    path('outer',views.main_dashboard, name='outer')

]