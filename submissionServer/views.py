from django.shortcuts import render
from django.http import HttpResponse

from .models import Submission

# Create your views here.
def index(request):
    submissions = Submission.objects.order_by('date')[:5]
    context = {"submissions":submissions}
    return render(request, "index.html", context)

#made a change