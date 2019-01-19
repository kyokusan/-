from django.shortcuts import render


def super(request):
    return render(request,"index.html")