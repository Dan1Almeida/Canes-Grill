from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# from pessoas.models import Pessoa



# Create your models here.
# Se tornara uma tabela no banco de dados

class Prato(models.Model):
    #Atributos da Classe
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_prato = models.CharField(
        max_length=100,
        verbose_name= "Nome do prato"
        )
    ingredientes = models.TextField(
        verbose_name= "Ingredientes"    
        )
    modo_preparo = models.TextField(
        verbose_name= "Modo de preparo"
        )
    tempo_preparo = models.PositiveIntegerField(
        verbose_name="Tempo de preparo"
        )
    rendimento = models.CharField(
        max_length=100,
        verbose_name= "Rendimento"
        )
    categoria = models.CharField(
        max_length=100,
        verbose_name= "Categoria"
        )
    date_prato = models.DateTimeField( 
        default=datetime.now,
        blank = True
        )
    publicado = models.BooleanField(default=False)

    foto_prato = models.ImageField(
        upload_to = 'pratos/%Y/%m',
        blank = True,
    )
    
    def __str__(self): #Retorna o Nome do Prato
        return self.nome_prato
    
    class Meta: 
        verbose_name='Prato'
        verbose_name_plural ='Pratos'
    