from django.contrib import admin

# Register your models here.
from .models import Pessoa


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome','email',)
    list_display_links = ('id','nome',)
    list_editable = ['email']


admin.site.register(Pessoa, ListandoPessoas)