from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def list_terrenos(request):
    print("Hola desde terrenos")
    return HttpResponse("<h1>Hola desde terrenos</h1>")


def admin_terrenos(request):
    #Contectarme a las bd y consultar
    terrenos_list = [{
        "name": "Los Manguitos",
        "medidas": "100 m2",
    },
        {
            "name": "Magueyito",
            "medidas": "300 m2",
        },
        {
            "name": "Los Pajaros",
            "medidas": "122 m2",
        },
        {
        "name": "La reliqia",
        "medidas": "145 m2",
    }]
    context = {"terrenos_list": terrenos_list}
    return render(
        request,
        "base.html",
        context=context
    )