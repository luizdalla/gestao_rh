from django.contrib import admin
from .models import Funcionario



class FuncionarioAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_display = ('nome', 'empresa', 'idade')
    list_filter = ('empresa',)
    
admin.site.register(Funcionario, FuncionarioAdmin)
    
 