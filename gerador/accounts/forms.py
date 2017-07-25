from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Forms são utilizados com Django para facilitar a apresentação dos campos de um formulário
# em seu template. Neste caso estou utilizando um form pré-formatado (UserCreationForm)
# mas com alterações para que além do usuário e das senhas, também pegue o e-mail do usuário.


class RegisterForm(UserCreationForm):
    # Meta define os campos do banco de dados que serão preenchidos com o form
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Definindo que tipo de campo 'email' deve ser no template
    email = forms.EmailField(label='E-mail')

    # Função para verificar se o e-mail já está cadastrado
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email

    # Função pré-formatada com alterações para que o email também seja salvo
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user