from django.shortcuts import render
from django.core.mail import send_mail
from events_app.models import Wine
from events_app.forms import EmailPostForm


# Create your views here.
def display_wine(request):
    all_wine = Wine.objects.all()

    return render(request,
                  'wine.html',
                  {'all_wine': all_wine})

def display_contact(request):
    sent = False
    form = EmailPostForm(request.POST)

    if request.method == 'POST':
        # form was submitted
        if form.is_valid():
            # send email
            cd = form.cleaned_data
            subject = f"Message de {cd['name']}"
            message = f"Message de la part de: {cd['email']}\n\n{cd['message']}"

            send_mail(subject,
                      message,
                      'info@eilinoyaevents.com',
                      ['info@eilinoyaevents.com'])
            sent = True
    else:
        form = EmailPostForm()

    return render(request,
                  'contact.html',
                  {'sent': sent,
                   'form': form})


def index(request):
    all_wine = Wine.objects.all()

    return render(request,
                  'index.html',
                  {'all_wine': all_wine})
