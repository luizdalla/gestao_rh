from django.urls import path
from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete, FuncionariosCreate, PdfReportLab, Pdf


urlpatterns = [
    # path('', home),
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario'),
    path('criar/', FuncionariosCreate.as_view(), name='create_funcionario'),
    path('pdf-reportlab/', PdfReportLab, name='pdf_reportlab'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='pdf_funcionarios_html'),
]