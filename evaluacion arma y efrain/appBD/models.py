from django.db import models

# Create your models here.
class alumnos(models.Model):
    ALUMRUT=models.CharField(max_length=12)
    ALUMNOMBRE=models.CharField(max_length=15)
    ALUMAPATERNO=models.CharField( max_length=15)
    ALUMAMATERNO=models.CharField(max_length=15)
    ALUMDIRECCION=models.CharField(max_length=60)
    ALUMEMAIL=models.CharField(max_length=40)
    ALUMNFONO=models.CharField(max_length=15)

class tipo_cursos(models.Model):
    TIPCURNOMBRE=models.CharField(max_length=15) 
    TIPCURVALOR=models.IntegerField(max_length=11)

class matriculas(models.Model):
    MATNUMERO=models.SmallIntegerField(max_length=11)

class ciudades(models.Model):
    CIUNOMBRE=models.CharField(max_length=20)
    
class sucursales(models.Model):
    CIUCODIGO=models.ForeignKey(ciudades,on_delete=models.CASCADE)
    SUCNOMBRE=models.CharField(max_length=20)

    
class usuarios(models.Model):
    USULOGIN=models.CharField(max_length=15)
    USUPASSWORD=models.CharField(max_length=15)
