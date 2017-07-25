from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import RegisterForm

# Em Django as views são criadas para carregar suas páginas HTML e definir o processamento que devem executar

# Criando a view register, que retorna a página "register.html"
# Define como caminho "accounts/register.html" pois é o caminho base do form já fornecido pelo Django
# Verifica se o methodo de chamada da view é um POST
# Se o méodo for 'POST' pega os dados do formulário e os envia para o form 'RegisterForm' 
# e em seguida salva seus dados no banco de dados
# Se não for 'POST' (Normalmente um 'GET'), apenas chama o método form 
# para que os campos possam ser apresentados no template 'register.html'
# A view register também retorna em seu contexto a variável 'form', como 'form' para o template.
def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})