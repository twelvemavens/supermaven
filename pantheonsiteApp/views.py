from django.shortcuts import render


def home(request):
    context = {}
    template = 'pantheonsiteApp/companies.html'
    return render(request, template, context)

def detail(request):
    context = {}
    template = 'pantheonsiteApp/48forty-solutions.html'
    return render(request, template, context)