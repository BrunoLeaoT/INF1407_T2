from django.urls.conf import path
from Catalogo import views

app_name = 'Catalogo'

urlpatterns = [
    path('image-info', views.imageInfo,name='image-info'),
]
