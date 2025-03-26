from django.shortcuts import render

# Create your views here.
def unipage(request):
    return render(request, "unipage/main.html")

def land(request):
    return render(request, "unipage/landing.html")