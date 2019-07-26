from django.db import models

# Create your models here.
# CODING FIRST: PRIMEIRO ESCREVE O CÓDIGO COM A ESTRUTURA DO BANCO, DEPOIS DE RODAR UM COMANDO É CRIADO O BANCO
# DE DADOS.
class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    )

    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome'
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name = 'Sobrenome'
    )

    genero = models.CharField(
        max_length = 255,
        verbose_name = 'Gênero',
        choices = GENEROS
    )

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail',
        blank = False # com o blank=false retorna erro se o o usuário não preencher esse campo, por padrao já é false
    )

    biografia = models.TextField(
        null = True,
        blank = True
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome