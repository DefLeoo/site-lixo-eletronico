from django.db import models

class Registrado(models.Model):
    nome = models.CharField(max_length=100 , blank= True, null= True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add= True, auto_now=False)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email