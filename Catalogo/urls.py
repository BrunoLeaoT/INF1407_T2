from django.urls.conf import path
from Catalogo import views
from LeaoMarinho import accountViews
app_name = 'Catalogo'

urlpatterns = [
    path('home/', views.home,name='catalogos'),
    path('ver-catalogo/<str:id>/<str:nome>', views.catalogo,name='ver-catalogo'),
    path('edit-catalogo/<str:nome>', views.editCatalogo,name='edit-catalogo'),
    path('add-catalogo/', views.adicionarNovoCatalogo,name='add-catalogo'),
    path('apagar-catalogo/<str:nome>', views.apagarCatalogo,name='apagar-catalogo'),
    path('editar-individuo/<str:id>', views.editarIndividuo,name='editar-individuo'),
    path('apagar-individuo/<str:id>', views.removerIndividuo,name='apagar-individuo'),
    path('add-individuo/<str:nome>', views.adicionarIndividuo,name='add-individuo'),
    path('', accountViews.home,name='home'),
] 
