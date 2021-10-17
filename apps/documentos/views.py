from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from apps.documentos.models import Documento
from django.contrib.auth.models import User


# class FuncionariosList(ListView):
#     model = Funcionario
    
#     def get_queryset(self):
#         empresa_logada = self.request.user.funcionario.empresa
#         return Funcionario.objects.filter(empresa = empresa_logada)
        
        
# class FuncionariosEdit(UpdateView):
#     model = Funcionario
#     fields = ['nome', 'departamento']
    
# class  FuncionariosDelete(DeleteView):
#     model = Funcionario
#     success_url = reverse_lazy('list_funcionarios')
    
class DocumentoCreate(CreateView):
    model =Documento
    fields = ['descricao', 'arquivo']
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        