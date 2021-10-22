from django.urls import path
# from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete, FuncionariosCreate
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate, HoraExtraEditBase, UtilizouHoraExtra, NaoUtilizouHoraExtra, ExportarParaCSV, ExportarExcel


urlpatterns = [
    # path('', home),
    path('', HoraExtraList.as_view(), name='list_horaextra'),
    path('editar_funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_horaextra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_horaextra_base'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horaextra'),
    path('criar/', HoraExtraCreate.as_view(), name='create_horaextra'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtra.as_view(), name='nao_utilizou_hora_extra'),
    path('exportar-csv', ExportarParaCSV.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),
]