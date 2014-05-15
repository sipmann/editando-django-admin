from django.db import models

class comentario(models.Model):
	nome = models.CharField(max_length=30)
	texto = models.TextField()
	liberado = models.BooleanField()
	data = models.DateField()
	
	def __unicode__(self):
		return self.texto[0:20]