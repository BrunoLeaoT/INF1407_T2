from django.shortcuts import render
from LeaoMarinho.controller.usersController import UserController
from django.http.response import HttpResponseRedirect
userController = UserController()
# Create your views here.
def home(request):
	print("rest")
	return render(request, 'account/index.html')

def login(request):
	print("login")
	return render(request, 'account/login.html')

def create(request):
	if request.method == 'POST':
		user = request.POST['user']
		senha = request.POST['senha']
		confirmaSenha = request.POST['confirmaSenha']
		res = userController.create(user,senha)
		if res:
			print(res)
			HttpResponseRedirect(request,'account:login')
		else:
			HttpResponseRedirect(request, 'account:registro')
	else:
		return render(request, 'account/registro.html')