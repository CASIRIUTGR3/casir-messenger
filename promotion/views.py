from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
               "message": "Page d'accueil",
               }
    
    return render(request, "promotion/index.html", context)