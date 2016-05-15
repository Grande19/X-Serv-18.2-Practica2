from django.shortcuts import render
from models import Uri
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def form(request):

    salida = ''
    url = ''
    formulario = '<form method = "POST">'
    formulario += 'Acortador url : <input type = "text" name = "valor" >'
    formulario += '<input type ="submit" value = "Enviar" >'
    formulario += '</form>'
    lista = Uri.objects.all() #muestra todo lo que tenemos en la base de datos

    if request.method == 'POST':
        if request.POST['valor'].find('http') == -1 :
            url = 'http://' + request.POST['valor']
        else :
            url = request.POST['valor']

    for fila in lista:
        if fila.url == url :
            return HttpResponse ('La url' + url + 'acortada' + 'con ID = ' + str(fila.id))


    db = Uri (url = url)
    db.save()


    lista = Uri.objects.all()
    salida = 'Lista de urls acortadas :' + '<br>'
    for fila in lista :
        salida += '<li>' + fila.url + ' , ID = ' + str(fila.id)

    return HttpResponse (formulario + '<br>' + salida)

    def Busqueda (request, recurso):
        try :
            db = Uri.objects.get(id=recurso)
            return HttpResponseRedirect(db.url)
        except Uri.DoesNotExist:
            return HttpResponse('Recurso/' + recurso + 'no encontrado')
