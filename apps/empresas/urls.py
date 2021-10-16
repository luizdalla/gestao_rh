from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('nova', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>', EmpresaEdit.as_view(), name='edit_empresa'),
]