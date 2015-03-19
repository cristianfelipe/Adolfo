from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('catalogo.apps.home.views',
	    url(r'^$','paginaprincipal_view', name = 'vista_principal'),    
	    url(r'^about/$', 'about_view', name = 'vista_about'),
	    url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
	    url(r'^login/$', 'login_view', name = 'vista_login'),
	    url(r'^logout/$', 'logout_view', name = 'vista_logout'),
	    url(r'^juguetes/page/(?P<pagina>.*)/$','juguetes_view', name = 'vista_juguetes'),
		url(r'^juguete/(?P<id_juguete>.*)/$', 'single_juguete_view', name = 'vista_juguete'),
	)	    