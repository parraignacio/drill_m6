from django.contrib import admin
from .models import VehiculoModel

admin.site.site_header = 'Final Drilling M6: Ignacio Parra'
admin.site.index_title = 'Panel de control Proyecto Django'


class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'get_condicion', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('modelo__startswith', 'serial_carroceria')
    
    def get_condicion(self, obj):
        return obj.get_condicion()
    get_condicion.short_description = 'Condición de Precio'


admin.site.register(VehiculoModel, VehiculoAdmin)
