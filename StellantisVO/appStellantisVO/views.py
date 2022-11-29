from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(requests, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))


def soma(requests, int1, int2):
    total = int1 + int2
    return HttpResponse('<h2>A soma é: {}'.format(total))
