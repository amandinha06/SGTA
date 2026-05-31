from django.urls import path
from . import views

urlpatterns = [

    # GET
    path('tarefas/', views.listar_tarefas),
    path('tarefas/abertas/', views.listar_tarefas_abertas),
    path('tarefas/urgentes/', views.tarefas_urgentes),
    path('tarefas/nao_urgente/', views.tarefas_nao_urgente),
    path('tarefas/<int:id>/', views.buscar_id),
    path('tarefas/dupla/', views.busca_dupla),
    path('tarefas/atrasadas/', views.tarefas_atrasadas),
    path('tarefas/busca/<str:palavra>/', views.busca_palavra),

    # POST
    path('tarefas/criar/', views.criar_tarefa),

    # PUT
    path('tarefas/<int:id>/atualizar/', views.atualizar_tarefa),

    # DELETE
    path('tarefas/<int:id>/remover/', views.remover_tarefa),
]
