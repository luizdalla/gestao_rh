from django.urls import path
from .views import DocumentoCreate


urlpatterns = [
    # path('', home),
    # path('', FuncionariosList.as_view(), name='list_funcionarios'),
    # path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionario'),
    # path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario'),
    path('criar/<int:funcionario_id>', DocumentoCreate.as_view(), name='create_documento'),
]