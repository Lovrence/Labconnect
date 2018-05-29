from django.shortcuts import render

def labconnect(request):
    return render(request, 'frontend/welcome.html', locals)