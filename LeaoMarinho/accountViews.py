from django.shortcuts import render, redirect
from LeaoMarinho.controller.usersController import UserController
from django.http.response import HttpResponse
from pymongo import MongoClient
from hashlib import sha256
from bson.objectid import ObjectId
from hashlib import sha256
import random
userController = UserController()
database = 'mongodb+srv://bruno:br11do12@cluster0.iuukf.mongodb.net/test'
client = MongoClient(database)
db=client.inf1013

def home(request):
	return render(request, 'account/index.html')

def catalogos(request):
	userId = request.session.get('userId')
	print(userId)
	catalogosDB = db.catalogos.find({'user': ObjectId(userId)})
	
	catalogos = []
	for catalogo in catalogosDB:
		catalogoAux = {}
		catalogoAux['nome'] = catalogo['nome']
		catalogoAux['id'] = str(catalogo['_id'])
		catalogos.append(catalogoAux)
	print(catalogos)
	return render(request,'catalogo/home.html',{'catalogos':catalogos})

def login(request):
	if request.method == 'POST':
		user = request.POST['user']
		senha = request.POST['senha']
		res = userController.login(user,senha)

		if res:
			request.session['userId'] = str(res['_id'])
			return render(request, 'account/index.html')
		else:
			return render(request, 'account/login.html', {'erro':'Senha inválida'})
	else:
		return render(request, 'account/login.html')

def logout(request):
	del request.session['userId']
	return render(request, 'account/index.html')

def create(request):
	if request.method == 'POST':
		user = request.POST['user']
		senha = request.POST['senha']
		confirmaSenha = request.POST['confirmaSenha']

		# Verificar se senhas são compativeis
		if (senha != confirmaSenha):
			return render(request,'account/registro.html',{'erro':'Senhas não compativeis'})

		res = userController.create(user,senha)
		if res:
			return render(request,'account/login.html')
		else:
			render(request, 'account/registro.html')
	else:
		return render(request, 'account/registro.html')

def mudarSenha(request):
	print("Eu odeio django")
	if request.method == 'POST':
		senhaAntiga = request.POST['senhaAntiga']
		senhaNova = request.POST['senhaNovo']
		confirmacaoSenha = request.POST['confirmaSenha']
		userId = request.session.get('userId')
		user = db.users.find_one({'_id': ObjectId(userId)})
		if (user['password'] == sha256(senhaAntiga.encode('utf-8')).hexdigest()):
			if(senhaNova == confirmacaoSenha):
				db.users.find_one_and_update({'_id': ObjectId(userId)},{'$set': {'password': sha256(senhaNova.encode('utf-8')).hexdigest()}})
				return render(request, 'account/index.html')
			else:
				return render(request, 'account/mudar-senha.html', {'erro':'Senhas incompativeis'})
		else:
			return render(request, 'account/mudar-senha.html', {'erro':'Senha antiga incorreta'})
	else:
		return render(request, 'account/mudar-senha.html')

def changePicture(request):
	picNumber = random.randint(1,3)
	filename = 'whale'+str(picNumber)+'.png'
	return HttpResponse(filename)