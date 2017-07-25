from django import forms
from .models import Questionario

# Declarando a variável que apresentará as escolhas para o usuário
# Recebe uma tupla, em que o primeiro conteúdo é o valor que será registrado na base de dados
# e o segundo será a forma que será apresentado para o usuário
CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5,'5'))

# Cria o form 'QuizForm' que definirá como devem ser apresentados os campos para o usuário preencher
class QuizForm(forms.ModelForm):
	# Seleção dos campos da tabela(modelo) Questionario que devem ser apresentados
	class Meta:
		model = Questionario
		fields = ('primeiraresposta_questionario', 'segundaresposta_questionario', 'terceiraresposta_questionario', 'quartaresposta_questionario')

	# Define que o campo será um 'choice field', com a pergunta em uma label, com botões 'radio' 
	# e que as escolhas são as definidas em CHOICES
	primeiraresposta_questionario = forms.ChoiceField(
		label = 'O poema gerado está coerente? Dê uma nota. (1 menor nota, 5 maior nota)',
		widget = forms.RadioSelect,
		choices = CHOICES
	)
	segundaresposta_questionario = forms.ChoiceField(
		label = 'O poema gerado está coeso? Dê uma nota. (1 menor nota, 5 maior nota)',
		widget = forms.RadioSelect,
		choices = CHOICES
	)

	# Determina que o campo será um 'choice field', com a pergunta em uma label, com botões 'radio'
	# e que as escolhas são 'Sim' e 'Não'
	terceiraresposta_questionario = forms.ChoiceField(
		label = 'O poema gerado está de acordo com a restrição selecionada?',
		widget = forms.RadioSelect,
		choices = (('Sim', 'Sim'), ('Não', 'Não'))
	)

	quartaresposta_questionario = forms.ChoiceField(
		label = 'O poema gerado apresenta algum erro de sintáxe?',
		widget = forms.RadioSelect,
		choices = (('Sim', 'Sim'), ('Não', 'Não'))
	)