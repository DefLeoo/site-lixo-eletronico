from django.shortcuts import render
from .forms import RegModelForm, ContatoForm
from .models import Registrado

def inicio(request):
    titulo = "BEM VINDO"
    if request.user.is_authenticated():
          titulo = "Bem vindo %s" %(request.user)
    form = RegModelForm(request.POST or None)
    context = {
           "titulo": titulo,
           "el_form":form,
     }

    if form.is_valid():
        instance = form.save(commit = False)
        nome = form.cleaned_data.get("nome")
        email = form.cleaned_data.get("email")
        if not instance.nome:
            instance.nome = "pessoa"
        instance.save()

        context = {
            "titulo": "thanks %s!" % (nome)
        }
        if not nome:
            context = {
                "titulo" : "thanks %s !"%(email)

            }

        print(instance)
        print(instance.timestamp)
        #form_data = form.cleaned_data
        #abc = form_data.get("email")
        #abc2 = form_data.get("nome")
        #obj = Registrado.objects.create(email=abc, nome=abc2)
    return render(request,"inicio.html",context)

def contato(request):
    titulo = "Fale conosco"
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key,value)
    context = {
        "form":form,
        "titulo":titulo,

    }
    return render(request, "forms.html", context)