from  django.shortcuts import  render

def about(request):
    return render(request,"about.html", {})


def page(request):
    return render(request,"page.html", {})

def detalhes(request):
    return render (request,"detalhes.html",{})

def lixo(request):
    return render(request,"lixo.html",{})

def solucoes(request):
    return render(request,"solucoes.html",{})