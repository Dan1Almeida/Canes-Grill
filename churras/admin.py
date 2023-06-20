from django.contrib import admin


# EDITA A BASE DO ADMIN (Churras)

from .models import Prato

class ListandoPratos(admin.ModelAdmin):
    list_display = [ 
        'id','nome_prato','categoria','tempo_preparo','rendimento','pessoa_id','publicado'
    ]
    list_display_links = [
        'id','nome_prato'
    ]
    search_fields = ['nome_prato']
    list_editable = ['categoria','publicado']
    ordering = ['id',] #Ordenar do menor para o maior
    list_filter = ['categoria']
    list_per_page = 10


admin.site.register(Prato, ListandoPratos)

# Register your models here.
