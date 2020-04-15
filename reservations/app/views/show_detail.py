from django.shortcuts import render
from django.http import HttpResponse

def show (request, id_Shows) :

    return HttpResponse (
    "vue comprenant un show" )