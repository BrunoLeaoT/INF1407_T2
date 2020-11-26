from django.shortcuts import render

# Create your views here.
def catalogo(request):
    return render(request, 'Catalogo/home.html')

def imageInfo(request):
    # processamento antes de mostrar
    # a segunda página
    return render(request, 'Catalogo/image.html')
