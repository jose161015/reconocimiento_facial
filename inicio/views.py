from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'inicio/index/index.html')


def login_view(request):
	if request.method=='POST':
		username=request.POST['usuario']
		password=request.POST['pass']
		user=authenticate(request, username=username,password=password)
		if user is not None:
			login(request,user)
			if user.is_superuser:
				return redirect('/admin/')
			else:
				return redirect('index')
		else:
			return render(request, 'login/login.html',{'error':'Usuario o contraseña invalido'})
	return render(request, 'login/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')