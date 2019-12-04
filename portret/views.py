from django.shortcuts import render
from .models import Assignment, Job, Activity
from django.db.models import Prefetch, Count
def home(request):
    return render(request, 'portret/home.html')

def overmij(request):
    return render(request, 'portret/overmij.html')

def cv(request):
    assignment_list = Assignment.objects.order_by('-startdate').all().prefetch_related(Prefetch('job',queryset=Job.objects.all(), to_attr='job_list'))
    assignment_list = assignment_list.annotate(aantal_jobs=Count('job'))
    activity_list = Activity.objects.order_by('startdate','jobtitle','rownumber').all()

    context = {
        'assignment_list': assignment_list,
        'activity_list': activity_list
    }
    return render(request, 'portret/cv.html', context)