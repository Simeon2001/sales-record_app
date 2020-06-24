from django.shortcuts import render
from .models import Sales
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    ur = Sales.objects.order_by('-id')
    return render(request, 'index.html',{'ur':ur})

class SalesCreateView(CreateView):
    model = Sales
    template_name = 'form.html'
    success_url = reverse_lazy('Home')
    fields = ['client','end_user','description','model_serial_no','qty','gate_pass','category','sales_date']
    
    
class SalesUpdateView(UpdateView):
    model = Sales
    template_name = 'update.html'
    success_url = reverse_lazy('Home')
    fields = ['client','end_user','description','model_serial_no','qty','gate_pass','category','sales_date']
    
    
class SalesDeleteView(DeleteView):
    model = Sales
    template_name = 'delete.html'
    success_url = reverse_lazy('Home')