from django.urls import path
# from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete, FuncionariosCreate
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate, HoraExtraEditBase


urlpatterns = [
    # path('', home),
    path('', HoraExtraList.as_view(), name='list_horaextra'),
    path('editar_funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_horaextra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_horaextra_base'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horaextra'),
    path('criar/', HoraExtraCreate.as_view(), name='create_horaextra'),
]