from django.urls import path
from .views import listar_tarefas
from .views import listar_tarefas_abertas
from .views import tarefas_urgentes
from .views import tarefas_nao_urgente
from .views import buscar_id
from .views import busca_dupla
from .views import tarefas_atrasadas
from .views import busca_palavra

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('abertas/', listar_tarefas_abertas),
    path('urgentes/', tarefas_urgentes),
    path('naourgentes/', tarefas_nao_urgente),
    path('tarefas/<int:id>/', buscar_id),
    path('abertasugentes/', busca_dupla),
    path('atrasadas/', tarefas_atrasadas),
    path('tarefas/<str:palavra>/', busca_palavra)
]

# rotas
