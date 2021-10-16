from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from apps.departamentos.models import Departamento
from django.contrib.auth.models import User

class DepartamentosList(ListView):
    model = Departamento
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa = empresa_logada)
        
        
class DepartamentosEdit(UpdateView):
    model = Departamento   
    fields = ['nome', 'empresa']
    
class  DepartamentosDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
    
class DepartamentosCreate(CreateView):
    model =Departamento
    fields = ['nome']
    
    def form_valid(self,form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)
        