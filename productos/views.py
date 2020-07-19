from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home_view():
    return HttpResponse("<h1> Saraswati App </h1>")

