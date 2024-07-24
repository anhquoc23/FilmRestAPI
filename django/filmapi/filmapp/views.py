from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.

def home(req):
    return TemplateResponse(req, 'index.html')