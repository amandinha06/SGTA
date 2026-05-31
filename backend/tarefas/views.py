from django.http import JsonResponse
from .models import Tarefa
from datetime import date
import json
from django.views.decorators.csrf import csrf_exempt


# GET - listar todas
def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)


# GET - tarefas abertas
def listar_tarefas_abertas(request):
    tarefas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas), safe=False)


# GET - urgentes
def tarefas_urgentes(request):
    tarefas = Tarefa.objects.filter(prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)


# GET - não urgentes
def tarefas_nao_urgente(request):
    tarefas = Tarefa.objects.filter(prioridade='NAO_URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)


# GET - buscar por ID
def buscar_id(request, id):
    tarefa = Tarefa.objects.filter(id=id).values()
    return JsonResponse(list(tarefa), safe=False)


# GET - busca dupla
def busca_dupla(request):
    tarefas = Tarefa.objects.filter(
        status='ABERTA',
        prioridade='URGENTE'
    ).values()

    return JsonResponse(list(tarefas), safe=False)


# GET - atrasadas
def tarefas_atrasadas(request):
    hoje = date.today()

    tarefas = Tarefa.objects.filter(
        data_entrega__lt=hoje
    ).values()

    return JsonResponse(list(tarefas), safe=False)


# GET - busca palavra
def busca_palavra(request, palavra):
    tarefa = Tarefa.objects.filter(
        titulo__icontains=palavra
    ).values()

    return JsonResponse(list(tarefa), safe=False)


# POST - criar tarefa
@csrf_exempt
def criar_tarefa(request):

    if request.method == 'POST':

        dados = json.loads(request.body)

        tarefa = Tarefa.objects.create(
            titulo=dados['titulo'],
            descricao=dados['descricao'],
            status=dados['status'],
            prioridade=dados['prioridade'],
            data_entrega=dados['data_entrega'],
            usu_responsavel_id=dados['usu_responsavel']
        )

        return JsonResponse({
            'id': tarefa.id,
            'mensagem': 'Tarefa criada com sucesso'
        })

    return JsonResponse({
        'erro': 'Método não permitido'
    }, status=405)

# PUT - atualizar tarefa
@csrf_exempt
def atualizar_tarefa(request, id):

    if request.method == 'PUT':

        dados = json.loads(request.body)

        try:

            tarefa = Tarefa.objects.get(id=id)

            tarefa.titulo = dados['titulo']
            tarefa.descricao = dados['descricao']
            tarefa.status = dados['status']
            tarefa.prioridade = dados['prioridade']
            tarefa.data_entrega = dados['data_entrega']
            tarefa.usu_responsavel_id = dados['usu_responsavel']

            tarefa.save()

            return JsonResponse({
                'mensagem': 'Tarefa atualizada com sucesso'
            })

        except Tarefa.DoesNotExist:

            return JsonResponse({
                'erro': 'Tarefa não encontrada'
            }, status=404)

    return JsonResponse({
        'erro': 'Método não permitido'
    }, status=405)


# DELETE - remover tarefa
@csrf_exempt
def remover_tarefa(request, id):

    if request.method == 'DELETE':

        try:
            tarefa = Tarefa.objects.get(id=id)

            tarefa.delete()

            return JsonResponse({
                'mensagem': 'Tarefa removida com sucesso'
            })

        except Tarefa.DoesNotExist:
            return JsonResponse({
                'erro': 'Tarefa não encontrada'
            }, status=404)

    return JsonResponse({
        'erro': 'Método não permitido'
    }, status=405)