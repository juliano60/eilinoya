from django.shortcuts import render
from events_app.models import Wine


# Create your views here.
def display_wine(request):
    all_wine = Wine.objects.all()

    return render(request,
                  'wine.html',
                  {'all_wine': all_wine})

def display_contact(request):
    context = {}
    return render(request,
                  'contact.html',
                  context)


def index(request):
    context = {}

    return render(request,
                  'index.html',
                  context)
