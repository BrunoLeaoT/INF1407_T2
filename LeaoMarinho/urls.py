"""LeaoMarinho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Catalogo import views
from LeaoMarinho import accountViews
from django.urls import path
from django.urls import include
urlpatterns = [
    path('',accountViews.home, name='home'),
	path('login',accountViews.login, name='login'),
    path('logout',accountViews.logout, name='logout'),
	path('registro',accountViews.create, name='registro'),
    path('mudar-senha',accountViews.mudarSenha, name='mudar-senha'),
    path('catalogos',accountViews.catalogos, name='catalogos'),
    path('Catalogo/', include('Catalogo.urls')),
]
