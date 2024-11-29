from django.db import models

# Create your models here.
class alumnos(models.Model):
    ALUMRUT=models.CharField(max_length=12, unique=True)
    ALUMNOMBRE=models.CharField(max_length=15)
    ALUMAPATERNO=models.CharField( max_length=15)
    ALUMAMATERNO=models.CharField(max_length=15)
    ALUMDIRECCION=models.CharField(max_length=60)
    ALUMEMAIL=models.CharField(max_length=40)
    ALUMNFONO=models.CharField(max_length=15)

class tipo_cursos(models.Model):
    TIPCURCODIGO=models.SmallIntegerField(max_length=6, unique=True)
    TIPCURNOMBRE=models.CharField(max_length=15) 
    TIPCURVALOR=models.IntegerField(max_length=11)


class ciudades(models.Model):
    CIUCODIGO=models.SmallIntegerField(max_length=6, unique=True)
    CIUNOMBRE=models.CharField(max_length=20)
    
class sucursales(models.Model):
    SUCCODIGO=models.SmallIntegerField(max_length=6, unique=True)
    CIUCODIGO=models.ForeignKey(ciudades,on_delete=models.CASCADE)
    SUCNOMBRE=models.CharField(max_length=20)

class matriculas(models.Model):
    MATNUMERO=models.SmallIntegerField(max_length=11, unique=True)
    TIPCURCODIGO=models.ForeignKey(tipo_cursos,on_delete=models.CASCADE)
    ALUMRUT=models.ForeignKey(alumnos,on_delete=models.CASCADE)
    SUCCODIGO=models.ForeignKey(sucursales,on_delete=models.CASCADE)
    MATFECHA=models.DateField()


class usuarios(models.Model):
    USULOGIN=models.CharField(max_length=15)
    USUPASSWORD=models.CharField(max_length=15)
