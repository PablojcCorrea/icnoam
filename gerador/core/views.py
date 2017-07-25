from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
# Em Django as views são criadas para carregar suas páginas HTML e definir o processamento que devem executar
def home (request):
	return render(request, 'home.html')

def about (request):
	return render(request, 'about.html')