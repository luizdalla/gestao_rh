from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from apps.registros_hora_extra.models import RegistroHoraExtra
from apps.registros_hora_extra.forms import RegistroHoraExtraForm
from django.contrib.auth.models import User



class HoraExtraList(ListView):
    model = RegistroHoraExtra
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa = empresa_logada)
        
        
class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    # fields = ['motivo', 'funcionario', 'horas']
    form_class = RegistroHoraExtraForm
    
    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs 
    
    
    
class  HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horaextra')
    
class HoraExtraCreate(CreateView):
    model =RegistroHoraExtra
    # fields = ['motivo', 'funcionario', 'horas']
    form_class = RegistroHoraExtraForm
    
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs 