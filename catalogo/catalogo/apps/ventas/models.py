from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre        = models.CharField(max_length = 100)
	descripcion   = models.TextField(max_length = 500)

	def __unicode__():
		return self.nombre

class Marca(models.Model):
	nombre       =  models.CharField(max_length = 100)
	status       =  models.BooleanField(default = True)

	def __unicode__(self):
		return self.nombre		

class Etapa_juego (models.Model):
	rango		= models.CharField(max_length = 50)
	nombre      = models.CharField(max_length = 200)
	status      = models.BooleanField(default = True)

	def  __unicode__(self):
		return self.nombre

class Tipo_juguete (models.Model):
	nombre      = models.CharField(max_length = 200)
	status      = models.BooleanField(default = True)

	def  __unicode__(self):
		return self.nombre			

class Juguete(models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre, str (filename))
		return ruta
		
	nombre        = models.CharField(max_length = 100)
	dimension     = models.CharField(max_length = 500)
	status        = models.BooleanField(default = True)
	material      = models.CharField(max_length = 500)
	precio        = models.DecimalField(max_digits = 10, decimal_places = 2)
	marca         = models.CharField(max_length = 500)
	etapa_juego   = models.CharField(max_length =50)	
	tipo_juguete  = models.ManyToManyField(Tipo_juguete, null = True,blank = True)
	categorias    = models.ManyToManyField(Categoria, null = True,blank = True)      

	def __unicode__(self):
		return self.nombre




	


