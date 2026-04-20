# Create your views here.
# primeiro get 
from django.http import JsonResponse
from .models import Tarefa
from datetime import date

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)

def tarefas_urgentes(request):
    tarefas = Tarefa.objects.filter(prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

def tarefas_nao_urgente(request):
    tarefas = Tarefa.objects.filter(prioridade='NAO_URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)
    
def buscar_id(request, id):
    tarefa = Tarefa.objects.filter(id=id).values()
    return JsonResponse(list(tarefa), safe=False)
      
def busca_dupla(request):
    tarefas = Tarefa.objects.filter(status='ABERTA',prioridade='URGENTE' ).values() 
    return JsonResponse(list(tarefas), safe=False)

def tarefas_atrasadas(request):
    hoje = date.today()
    tarefas = Tarefa.objects.filter(data_entrega__lt=hoje).values()
    return JsonResponse(list(tarefas), safe=False)

def busca_palavra(request, palavra):
    tarefa = Tarefa.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefa), safe=False)