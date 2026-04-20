from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario

# Create your views here.
def listar_usuarios(request):
    usuario = Usuario.objects.all().values()
    return JsonResponse(list(usuario), safe=False)

from django.http import JsonResponse
from .models import Usuario

def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    
    return JsonResponse({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "ativo": usuario.ativo,
        "data_criacao": usuario.data_criacao
    })