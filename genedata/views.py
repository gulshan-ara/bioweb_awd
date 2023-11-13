from django.shortcuts import render
from .models import *

# Index function promised in urls
def index(request):
  # fetching values from Gene table
  genes = Gene.objects.all()
  return render(request, 'genedata/index.html', { 'genes' : genes})

def gene(request, pk):
  # fetching values from Gene table
  gene = Gene.objects.get(pk=pk)
  return render(request, 'genedata/gene.html', { 'gene' : gene})
