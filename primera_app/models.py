from django.db import models

# Create your models here.

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)


class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField()


class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    comuna = models.CharField(max_length=50, null=False)


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10, null=True)

class biblioteca(models.Model):
    nombre = models.CharField(max_length=100, null=False )
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class libro(models.Model):
    biblioteca = models.CharField(biblioteca, on_delte=models.CASCADE)
    genero = models.CharField(max_length=15, null= False)
    titulo = models.CharField(max_length=50, null=False)
    Autor = models.CharField(Autor, on_delete=models.CASCADE)
    paginas = models.CharField(max_length=5, null=False)
    copias = models.CharField(max_length=6, null=False) 



