from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def show (request, id_Shows) :

    return HttpResponse (
    "vue comprenant un show" )