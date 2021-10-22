from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from apps.funcionarios.models import Funcionario
from django.contrib.auth.models import User
from django.views.generic import View


class FuncionariosList(ListView):
    model = Funcionario
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa = empresa_logada)
        
        
class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']
    
class  FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
    
class FuncionariosCreate(CreateView):
    model =Funcionario
    fields = ['nome', 'departamento']
    
    def form_valid(self,form):
        funcionario = form.save(commit=False)
        username=funcionario.nome.split(' ')[0]+funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)
    

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def PdfReportLab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(250, 810, "Relatorio de Funcionarios")
    
    # palavras = ['palavra1', 'palavra2', 'palavra3']
    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)
    
    str_ = 'Nome: %s | Hora Extra: %.2f'
    
    p.drawString(0, 800, "_"*150)
    
    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extra))
        y-=20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response
    # buffer.seek(0)
    # return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


from django.template.loader import get_template
from xhtml2pdf import pisa 


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')
            