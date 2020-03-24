from django.shortcuts import render, redirect
from . import forms
from .models import Opdracht, Functie, Activiteit, Opleidingen
from django.db.models import Prefetch, Count
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from JKloppenburg.settings import EMAIL_HOST_USER

def home(request):
    return render(request, 'portret/home.html')

def info(request):
    return render(request, 'portret/info.html')

def cv(request):
    opdracht_list = Opdracht.objects.order_by('-startdatum').all().prefetch_related(Prefetch('functie',queryset=Functie.objects.all(), to_attr='functie_list'))
    opdracht_list = opdracht_list.annotate(aantal_functies=Count('functie'))
    activiteit_list = Activiteit.objects.order_by('startdatum','functienaam','rijnummer').all()
    opleidingen_list = Opleidingen.objects.order_by('-startjaar', 'opleiding_id').all()

    context = {
        'opdracht_list': opdracht_list,
        'activiteit_list': activiteit_list,
        'opleidingen_list': opleidingen_list
    }
    return render(request, 'portret/cv.html', context)

def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            naam = request.POST.get('name', '')
            email = request.POST.get('email', '')
            bericht = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'naam': naam,
                'email': email,
                'bericht': bericht,
            }
            content = template.render(context)

            email = EmailMessage(
                "Nieuw bericht vanuit JKloppenburg",
                content,
                "JKloppenburg" +'',
#                ['info@jkloppenburg.com'],
                [EMAIL_HOST_USER],
                headers = {'Reply-To': email }
            )

            email.send()

            messages.success(request, 'Je bericht is verstuurd. Ik zal z.s.m. contact met je opnemen.')
            form = ContactForm()
            return render(request, 'portret/contact.html',{'form': form})
        else:
            messages.warning(request, "Je bericht is nog niet verstuurd. Er zit een fout in je invulvelden. Pas het a.j.b. aan en VERSTUUR nogmaals.")

    return render(request, 'portret/contact.html', {'form': form,})