from django.contrib import admin
from .models import *

# Register your models here.
# O 'admin.py' é o arquivo que configura quais modelos criados no projeto serão apresentados 
# no admin do Django no browser.
# Apresenta as tabelas Generos, Artigos, Autores, Questionario e Restricoes

class GeneroAdmin(admin.ModelAdmin):
	list_display = ['nome_genero', 'quantidade_artigo_genero']
	search_fields = ['nome_genero']

class ArtigoAdmin(admin.ModelAdmin):
	list_display = ['titulo_artigo', 'id_genero_artigo']
	search_fields = ['titulo_artigo', 'id_genero_artigo']

class QuestionarioAdmin(admin.ModelAdmin):
	list_display = ['id_restricao', 'data_resposta_questionario']
	search_fields = ['id_restricao', 'data_resposta_questionario']

admin.site.register(Generos, GeneroAdmin),
admin.site.register(Artigos, ArtigoAdmin),
admin.site.register(Autores),
admin.site.register(Questionario, QuestionarioAdmin),
admin.site.register(Restricoes)