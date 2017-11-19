from django import  forms
from .models import  Registrado


class RegModelForm(forms.ModelForm):
    class Meta:

       #nome = forms.CharField(max_length=100)
       #email = forms.EmailField()
       model = Registrado
       fields = ["nome" , "email"]

    #def clean_email(self):
        #email = self.cleaned_data.get("email")
        #email_base,proveeder = email.split("@")
        #dominio,extension = proveeder.split(".")
        #if not extension == "edu":
         #   raise forms.ValidationError("please extension .EDU")
        #return  email

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        return nome

class ContatoForm(forms.Form):
     nome = forms.CharField(required=False)
     email = forms.EmailField()
     mensagem = forms.CharField(widget=forms.Textarea)