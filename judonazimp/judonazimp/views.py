from django.shortcuts import render

def fhomepage(request):
    return render(request, 'index.html')
