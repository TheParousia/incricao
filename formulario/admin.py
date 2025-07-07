from django.contrib import admin

# Register your models here.
from .models import InscritoPernoite, LinkCode 
@admin.register(InscritoPernoite)
class InscritoPernoiteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_inscricao', 'usercode_usado')
    search_fields = ('nome', 'email')
    list_filter = ('data_inscricao', 'usercode_usado')
    ordering = ('-data_inscricao',)

@admin.register(LinkCode)
class LinkCodeAdmin(admin.ModelAdmin):
    list_display = ('usercode', 'data_criacao', 'data_expiracao', 'observacao')
    search_fields = ('usercode','observacao')
    list_filter = ('data_criacao', 'data_expiracao')
    ordering = ('-data_criacao',)