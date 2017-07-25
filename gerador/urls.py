"""poemGen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from gerador.core.views import *
from gerador.accounts.views import register
from gerador.pln.views import *
from django.contrib.auth import views

# Definição de todas as urls que podem ser chamadas no sistema
# Caso alguma view seja definida sem definir sua URL, o django apresenta uma mensagem de erro/página não encontrada
# As urls paterns definem como deve ser apresentada a url e qual view deve ser chamada.
urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),

    url(r'^about/', about, name='about'),

	url(r'^login/$', views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': 'home'}, name='logout'),
	url(r'^register/$', register, name='register'),

    url(r'^changenoun/$', changenoun, name='changenoun'),
    url(r'^nplusseven/$', nplusseven, name='nplusseven'),
    url(r'^snowball/$', snowball, name='snowball'),
    url(r'^queneau/$', queneau, name='queneau'),
    url(r'^abc/$', abc, name='abc'),
    url(r'^acronym/$', acronym, name='acronym'),

    url(r'^admin/', admin.site.urls),
] 
