from django.urls import path
from inicio.views import index,logout_view, login_view

urlpatterns = [
	path('login',login_view,name='login'),
 	path('index', index, name='index'),
	path('logout',logout_view,name='logout'),
	

]