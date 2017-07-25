from django.db import models
from datetime import datetime

# Create your models here.
# Models são também as tabelas que serão criadas no banco de dados

# Model Generos, contém o nome do genero e quantos artigos deste genero que existem.
# O ID dos models são gerados automaticamente ao executar a migração dos banco de dados.
# A função __str__ define qual campo deve ser utilizado para apresentar o genero no Django Admin.
class Generos(models.Model):
	nome_genero = models.CharField(max_length=20)
	quantidade_artigo_genero = models.PositiveIntegerField()

	def __str__(self):
		return self.nome_genero

# Model Artigos, contém o titulo, a quantidade de autores, o texto, a data de publicação e o id do gênero do artigo.
class Artigos(models.Model):
	titulo_artigo = models.CharField(max_length=250)
	quantidade_autores_artigo = models.PositiveIntegerField()
	texto_artigo = models.TextField()
	data_publicacao_artigo = models.DateField()
	id_genero_artigo = models.ForeignKey(Generos)

	def __str__(self):
		return self.titulo_artigo

# Model Autores, que contém o nome do autor e o id do artigo que escreveu.
class Autores(models.Model):
	nome_autor = models.CharField(max_length=50)
	id_artigo = models.ForeignKey(Artigos)

	def __str__(self):
		return self.nome_autor

# Model Restricoes, que contém o nome da restrição.
class Restricoes(models.Model):
	nome_restricao = models.CharField(max_length=20)

	def __str__(self):
		return self.nome_restricao

# Model Questionario, que contém as respostas das quatro questões do formulário de avaliação
# A data de resposta que é registrada automáticamente e o ID da restrição que ta sendo avaliada.
class Questionario(models.Model):
	primeiraresposta_questionario = models.IntegerField()
	segundaresposta_questionario = models.IntegerField()
	terceiraresposta_questionario = models.CharField(max_length=3)
	quartaresposta_questionario = models.CharField(max_length=3)
	data_resposta_questionario = models.DateField(default=datetime.now())
	id_restricao = models.ForeignKey(Restricoes)

	def __str__(self):
		return self.id_restricao.nome_restricao