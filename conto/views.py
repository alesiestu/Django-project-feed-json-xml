from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from conto.models import Bill

class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'bill'
    template_name = 'conto/index.html'
 
def get_queryset(self):
    return Notify.objects.all()






# Create your views here.
