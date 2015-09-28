from django.shortcuts import render, HttpResponse
import makemit
import os

def index(request):
    return render(request, 'index.jade');

def codeofconduct(request):
    with open(os.path.dirname(makemit.__file__)+'/static/docs/MakeMITCodeofConduct.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=MakeMITCodeofConduct.pdf'
        return response
    pdf.closed

def review2015(request):
    return render(request, 'review2015.jade');