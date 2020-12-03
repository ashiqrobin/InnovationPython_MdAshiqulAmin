from django.shortcuts import render

def hi(request):
    return render(request, 'FIRSTAPPLICATION/hi.html')