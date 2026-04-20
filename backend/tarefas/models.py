from django.db import models
from usuarios.models import Usuario
# Create your models here.

#banco de dados sqlight

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]
    PRIORIDADE = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente')
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE, default='NAO_URGENTE')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    
    usu_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True
    )
    
    def __str__(self):
        return self.titulo