from django.contrib import admin

from.models import Registrado

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nome","timestamp"]
    list_filter = ["timestamp"]
    list_editable = ["nome"]
    search_fields = ["email", "nome"]
    class Meta:
        model = Registrado

admin.site.register(Registrado)