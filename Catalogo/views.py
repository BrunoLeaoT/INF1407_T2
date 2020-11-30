from django.shortcuts import render
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import base64
database = 'mongodb+srv://bruno:br11do12@cluster0.iuukf.mongodb.net/test'
client = MongoClient(database)
db=client.inf1013

def redirectPadrão(request):
    catalogosDB =  db.catalogos.find({'user': ObjectId(request.session.get('userId')) })

    catalogos = []
    for catalogo in catalogosDB:
        catalogoAux = {}
        catalogoAux['nome'] = catalogo['nome']
        catalogoAux['id'] = str(catalogo['_id'])
        catalogos.append(catalogoAux)
    return render(request,'catalogo/home.html',{'catalogos':catalogos})

# Funções com relação catalogos
def home(request):
    return redirectPadrão(request)

def catalogo(request,id,nome):
    individuos = db.individuals.find({'catalogo': ObjectId(id)})
    newIndividuos = []
    for individuo in individuos:
        if(len(individuo['imagens']) > 0):
            imagem = db.images.find_one({'_id': ObjectId(individuo['imagens'][0])})
            individuo['imageBase64'] = imagem['image'].decode('utf-8')
        individuo['id'] = str(individuo['_id'])
        newIndividuos.append(individuo)
    return render(request, 'Catalogo/catalogo.html', {'individuos': newIndividuos,'nomeCatalogo':nome})

def adicionarNovoCatalogo(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        listaIndividuos = []
        userId = request.session.get('userId')
        catalogo = {}
        catalogo['nome'] = nome
        catalogo['individuos'] = listaIndividuos
        catalogo['user'] = ObjectId(userId)
        res = db.catalogos.insert_one(catalogo)
        print(res)
        return redirectPadrão(request)
    else:
        return render(request,'Catalogo/add-catalogo.html')

def editCatalogo(request,nome):
    if request.method == 'POST':
        nome = request.POST['nome']
        newNome = request.POST['newNome']
        print(newNome)
        try:
            print(nome)
            db.catalogos.find_one_and_update({'nome':nome}, {"$set": {'nome':newNome}})
            return render(request, 'Catalogo/edit-catalogo.html',{'nome': newNome,'result':'Editado'})
        except Exception as e:
            print(e)
            nome = request.POST['nome']
            return render(request, 'Catalogo/edit-catalogo.html',{'nome': nome,'result':'Algo deu errado'})
        
    else:
        return render(request, 'Catalogo/edit-catalogo.html',{'nome': nome})

def apagarCatalogo(request,nome):
    db.catalogos.delete_one({'nome': nome})
    return redirectPadrão(request)

# Funções Individuo
def adicionarIndividuo(request,nome):
    if request.method == 'POST':
        nomeIndividuo = request.POST['nome']
        especie = request.POST['especie']
        idCatalogo = request.POST['idCatalogo']
        print("inserindo individuo")
        try:
            imagem = request.FILES['file']  
            image_base64= base64.b64encode(imagem.read())
            _id = db.images.insert({'image': image_base64,'individuo':nomeIndividuo,'data':datetime.today().strftime('%Y-%M-%D')})
            db.individuals.insert_one({'nome': nomeIndividuo, 'especie':especie,'catalogo':ObjectId(idCatalogo) ,'imagens': [_id]})
            return redirectPadrão(request)
        except Exception as e:
            print(e)
            return render(request, 'Catalogo/add-individuo.html',{ 'erro':'Problema ao atualizar'})
                
    else:
        catalogo = db.catalogos.find_one({'nome':nome})
        return render(request, 'Catalogo/add-individuo.html', {'idCatalogo':catalogo['_id']})

def editarIndividuo(request,id):
    if request.method == 'POST':
        update = {}
        nome = request.POST['nome']
        especie = request.POST['especie']
        individuoId = request.POST['id']

        if(nome):
           update['individuo'] = nome
        if(especie):
            update['especie'] = especie

        try:
            db.individuals.update({'_id': ObjectId(individuoId)}, {"$set": update})
            return redirectPadrão(request)
        except Exception as e:
            print(e)
            return render(request, 'Catalogo/edit-individuo.html',{'id': individuoId, 'erro':'Problema ao atualizar'})
                
    else:
        return render(request, 'Catalogo/edit-individuo.html',{'id': id})

def removerIndividuo(request,id):
    try:
        db.individuals.delete_one({'_id': ObjectId(id)})
        return redirectPadrão(request)
    except Exception as e:
        return e
    