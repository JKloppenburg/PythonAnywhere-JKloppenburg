from django.shortcuts import render
from .models import Opdracht, Functie, Activiteit
from django.db.models import Prefetch, Count
def home(request):
    return render(request, 'portret/home.html')

def overmij(request):
    return render(request, 'portret/overmij.html')

def cv(request):
    opdracht_list = Opdracht.objects.order_by('-startdatum').all().prefetch_related(Prefetch('functie',queryset=Functie.objects.all(), to_attr='functie_list'))
    opdracht_list = opdracht_list.annotate(aantal_functies=Count('functie'))
    activiteit_list = Activiteit.objects.order_by('startdatum','functienaam','rijnummer').all()

    context = {
        'opdracht_list': opdracht_list,
        'activiteit_list': activiteit_list
    }
    return render(request, 'portret/cv.html', context)