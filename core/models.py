from django.db import models

class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=6)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome

class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    telefone = models.CharField('Telefone', max_length=22)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'