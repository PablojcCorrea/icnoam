from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

# Importar biblioteca spacy e random 
import spacy
import random

# Importar o análisador da Língua Inglesa, os modelos da aplicação pln e o formulário do questionário
from spacy.en import English
from .models import *
from .forms import QuizForm

# Criação do Analisador e Definição das variáveis globais
nlp = English()

Sentences = []

Poema = ['O poema gerado será apresentado aqui!']
Troca = ['O poema com substantivos trocados aparecerá aqui!']

Noun = [ ]
Det = [ ]
Verb = [ ]
Adj = [ ]
Adv = [ ]
Conj = [ ]

# Função para definir os modelos de sentenças que devem ser utilizados
def sentencePattern(localArray):
    localArray.append("DET ADJ NOUN ADV VERB DET NOUN .")
    localArray.append("ADJ, ADJ NOUN ADV VERB DET ADJ, ADJ NOUN .")
    localArray.append("NOUN VERB DET ADJ NOUN .")
    localArray.append("NOUN VERB !")
    localArray.append("ADV VERB DET NOUN VERB ?")
    localArray.append("NOUN, NOUN, CONJ NOUN .")
    localArray.append("ADV VERB DET ADJ NOUN ?")
    localArray.append("DET NOUN VERB ADJ, ADJ NOUN .")
    localArray.append("ADV VERB DET NOUN .")

sentencePattern(Sentences)

# Função que preenche a array sem repetições de palavras
def fill(arrayLocal, token):
    exist = 0
    for i in range(0, len(arrayLocal)):
        if(arrayLocal[i] == token.orth_):
            exist = 1
            break
    if(exist == 0):
        arrayLocal.append(token.orth_)

# Função para armazenar as palavras em suas matrizes
def fillArray(token):
    # Verifica o Part of Speech (pos_) para saber onde armazenar a palavra.
    if(token.pos_ == "ADJ"):
        fill(Adj, token)
    if(token.pos_ == "ADV"):
        fill(Adv, token)
    if(token.pos_ == "CONJ"):
        fill(Conj, token)
    if(token.pos_ == "DET"):
        fill(Det, token)
    if(token.pos_ == "NOUN"):
        fill(Noun, token)
    if(token.pos_ == "VERB"):
        fill(Verb, token)

# Função que gera os versos do poema e os armazena na área que é recebida por parâmetro
def sentenceMaker(arrayLocal, value):
        for i in range(0, value):
                sent = " "
                sentence = random.choice(Sentences)
                parsedPoem = nlp(sentence)
                for token in parsedPoem:
                        # Verifica se que tipo de palavra deve ser armazena da string
                        # e seleciona aleatóriamente uma palavra daquele Part of Speech
                        if(token.orth_ == "NOUN"):
                                sent = sent + " " + random.choice(Noun)
                        if(token.orth_ == "DET"):
                                sent = sent + " " + random.choice(Det)
                        if(token.orth_ == "VERB"):
                                sent = sent + " " + random.choice(Verb)
                        if(token.orth_ == "ADJ"):
                                sent = sent + " " + random.choice(Adj)
                        if(token.orth_ == "ADV"):
                                sent = sent + " " + random.choice(Adv)
                        if(token.orth_ == "CONJ"):
                                sent = sent + " " + random.choice(Conj)
                        if(token.pos_ == "PUNCT"):
                                sent = sent + token.orth_
                arrayLocal.append(sent)

# Função que troca os substantivos:
def change(sentence):
    parsedSentence = nlp(sentence)
    newSentence = ""
    for token in parsedSentence:
        # Verifica se a palavra sendo lida é um substantivo para trocá-lo por outro
        if(token.pos_ == "NOUN"):
            newSentence = newSentence + " " + random.choice(Noun)
        # Verifica se é uma pontuação, para que não haja espaçamento incorreto
        elif(token.pos_ == "PUNCT"):
            newSentence = newSentence + token.orth_
        # Reescreve a palavra analisa se ela não for um substantivo
        else:
            newSentence = newSentence + " " + token.orth_
    return newSentence

# Função para esvaziar as arrays globais
def cleanArrays():
    global Noun, Det, Verb, Adj, Adv, Conj

    Noun = []
    Det = []
    Verb = []
    Adj = []
    Adv = []
    Conj = []


# Create your views here.
# View para carregar o template 'changenoun.html' e retornar as variáveis necessárias para seu contexto
def changenoun (request):
    # Seleciona as variáveis globais que serão utilizadas
    global nlp, sentences, Poema, Troca
    cleanArrays()

    # Carrega todos os gêneros do banco de dados
    generos = Generos.objects.all()

    # Armazena o form que será apresentado e define quiz como 0 para que não seja apresentado no template
    quizForm = QuizForm()
    quiz = 0

    # Verifica se o método de chamada da view foi 'POST' e se foi feita pelo botão 'generatorbtn'
    # Gera o poema inicial
    if request.method == 'POST' and 'generatorbtn' in request.POST:
        # Se um arquivo for enviado, extrai as palavras, armazena elas como em 'text'
        if request.FILES:
            file = request.FILES['myfile']
            text = file.read()
        # Se não for enviado um arquivo, verifica que o ID do gênero selecionado é diferente de 0
        # Se for, define qual o ID selecionado, carrega em 'papers' todos os artigos daquele gênero
        # E seleciona aleatóriamente um deles, para colocar em 'text' 
        elif(request.POST.get('item_id1') != '0'):
            selected_gender = get_object_or_404(Generos, pk = request.POST.get('item_id1'))
            papers = Artigos.objects.filter(id_genero_artigo = selected_gender.id)
            paper = random.choice(papers)
            text = paper.texto_artigo
        
        # Cria o texto análisado, transformando cada palavra em um token
        # Para cada token em 'parsedText' chama a função de preencher arrays
        parsedText = nlp(str(text))
        for token in parsedText:
            fillArray(token)

        # Torna a variável global 'Poema' vazia
        # Gera 5 sentenças e as armazena em 'Poema', com 'sentenceMaker'
        # Define a variável troca com o conteúdo padrão
        Poema = []
        sentenceMaker(Poema, 8)
        Troca = ['O poema com substantivos trocados aparecerá aqui!']

    # Verifica se o método é 'POST' e que foi enviado pelo botão 'changebtn'
    # Faz a troca de substantivos
    if request.method == 'POST' and 'changebtn' in request.POST:
        if request.FILES:
            file = request.FILES['myfile2']
            text = file.read()
        elif(request.POST.get('item_id2') != '0'):
            selected_gender = get_object_or_404(Generos, pk = request.POST.get('item_id2'))
            papers = Artigos.objects.filter(id_genero_artigo = selected_gender.id)
            paper = random.choice(papers)
            text = paper.texto_artigo

        parsedText = nlp(str(text))

        for token in parsedText:
            fillArray(token)

        # Torna a variável global 'Troca' vazia
        # Envia para a função 'change' cada um dos versos do poema inical
        # Armazena em 'Troca' as sentenças com substantivos trocados
        Troca = []
        for i in range(0, len(Poema)):
            Troca.append(change(Poema[i]))

        # Define que quiz terá o valor 1, para que o formulário seja apresentado
        quiz = 1

    # Verifica se método é 'POST' e que foi enviado pelo botão 'sendbtn'
    if request.method == 'POST' and 'sendbtn' in request.POST:
        # Carrega as respostas no formulário
        quizForm = QuizForm(request.POST)
        # Verifica se o form é válido (se está completamente preenchido)
        if quizForm.is_valid():
            # Em new form força a carregar os dados sem salvar para que
            # em seguida possa apontar a restrição avaliada como 2 (Troca de Substantivo)
            # e salva os dados no banco de dados
            newform = quizForm.save(commit = False)
            newform.id_restricao_id = 2
            newform.save()
        else:
            # Se não for válido, retorna o form vazio
            quizForm = QuizForm()

    # Verifica se o método é um 'GET' (Quando carrega a página novamente)
    # Define 'Poema' e 'Troca' com o conteúdo padrão
    if request.method == 'GET':
        Poema = ['O poema gerado será apresentado aqui!']
        Troca = ['O poema com substantivos trocados aparecerá aqui!']
        # Retorna apenas a página que deve ser carregada, o conteúdo de Poem, Troca e os Gêneros como contexto
        return render(request, 'changenoun.html',{'content':Poema, 'changed':Troca, 'gender':generos})
    # Retorna a página que deve ser carregada, o conteúdo de Poema, Troca e os Gêneros, 
    # Bem como o formulário e a variável de controle que apresenta o form (quiz)
    return render(request, 'changenoun.html', {'content':Poema, 'changed':Troca, 'gender':generos, 'quizForm':quizForm, 'quiz':quiz})

# Abaixo seguem as views ainda sem processamento de linguagem natural
# São utilizadas para carregar suas respectivas páginas
def nplusseven (request):
    return render(request, 'nplusseven.html')

def snowball (request):
    return render(request, 'snowball.html')

def queneau (request):
    return render(request, 'queneau.html')

def abc (request):
    return render(request, 'abc.html')

def acronym (request):
    return render(request, 'acronym.html')