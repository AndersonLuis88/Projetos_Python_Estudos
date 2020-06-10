from django.db import models

class Base (models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Bolos(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    class Meta:
        verbose_name:'Bolo'
        verbose_name_plural = 'Bolos'

        def __str__(self):
            return self.titulo