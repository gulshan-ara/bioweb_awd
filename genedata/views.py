from django.shortcuts import render
from .models import *

# Index function promised in urls
def index(request):
  # fetching values from Gene table
  response_string = Gene.objects.all()[0]
  return render(request, 'genedata/index.html', { 'data' : response_string})
