# Create your views here.
from django.http import HttpResponse
from catalogo.apps.ventas.models import Juguete
from django.core import serializers


def ws_productos_view(request):
	data = serializers.serialize("json", Juguete.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')
	