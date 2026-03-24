from django.urls import path
from .views import listar_tarefas
from .views import listar_tarefas_abertas

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('abertas/', listar_tarefas_abertas)
]

# rotas
