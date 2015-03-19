from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('catalogo.apps.ventas.views',
		url(r'^add/juguete/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/juguete/(?P<id_prod>.*)/$','edit_producto_view', name = 'vista_editar_producto'),
	)

