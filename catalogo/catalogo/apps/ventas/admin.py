from django.contrib import admin
from  catalogo.apps.ventas.models import Categoria, Marca, Etapa_juego, Tipo_juguete, Juguete

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Etapa_juego)
admin.site.register(Tipo_juguete)
admin.site.register(Juguete)