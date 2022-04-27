from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import UserForm
from .diplom import replace_string
import mimetypes
# import os module
import os
from reportlab.pdfgen import canvas


# def index(request):
#     return render(request, 'main/index.html', {"form": UserForm})

userform = UserForm()
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        patronymic = request.POST.get("patronymic")
        print(lastname, 'gfdgdf')
        # age = request.POST.get("age")     # получение значения поля age
        # replace_string(lastname, name, patronymic)

        # return HttpResponse("""ку""")
        return getpdf(request, lastname, name, patronymic)
    else:

        # replace_string()
        # return render(request, "main/index.html")
        return render(request, "main/index.html", {"form": userform})
        # return render(request, "main/index.html", {"form": userform})

def single(request):
    return render(request, 'single.html')

def getpdf(request, lastname, name, patronymic):
    changes = lastname + ' ' + name + ' ' + patronymic
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,600, changes)
    p.showPage()
    p.save()
    return response
