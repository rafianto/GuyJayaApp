from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Cashflow
from .forms import CashflowForm

class CashflowListView(ListView):
    model = Cashflow
    template_name = 'cashflows/cashflows_list.html'
    context_object_name = 'cashflows'
    paginate_by = 10

def cashflow_create(request):
    if request.method == 'POST':
        form = CashflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cashflow_list')
    else:
        form = CashflowForm()
    
    return render(request, 'cashflows/cashflows_form.html', {
        'form': form,
        'title': 'Tambah Transaksi'
    })

def cashflow_update(request, pk):
    cashflow = get_object_or_404(Cashflow, pk=pk)
    if request.method == 'POST':
        form = CashflowForm(request.POST, instance=cashflow)
        if form.is_valid():
            form.save()
            return redirect('cashflow_list')
    else:
        form = CashflowForm(instance=cashflow)
    
    return render(request, 'cashflows/cashflows_form.html', {
        'form': form,
        'title': 'Edit Transaksi'
    })

def cashflow_delete(request, pk):
    cashflow = get_object_or_404(Cashflow, pk=pk)
    if request.method == 'POST':
        cashflow.delete()
        return redirect('cashflow_list')
    
    return render(request, 'cashflows/cashfloews_delete.html', {
        'cashflow': cashflow
    })