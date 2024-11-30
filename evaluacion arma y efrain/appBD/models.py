from django.db import models
from django.utils import timezone

# Create your models here.
class alumnos(models.Model):
    ALUMRUT=models.CharField(max_length=12, primary_key=True, default=1)
    ALUMNOMBRE=models.CharField(max_length=15)
    ALUMAPATERNO=models.CharField( max_length=15)
    ALUMAMATERNO=models.CharField(max_length=15)
    ALUMDIRECCION=models.CharField(max_length=60)
    ALUMEMAIL=models.CharField(max_length=40)
    ALUMNFONO=models.CharField(max_length=15)

    def __str__(self):
        return self.ALUMRUT
    

class tipo_cursos(models.Model):
    TIPCURCODIGO=models.IntegerField(max_length=6, primary_key=True, default=1)
    TIPCURNOMBRE=models.CharField(max_length=15) 
    TIPCURVALOR=models.IntegerField(max_length=11)

    def __str__(self):  
        return str(self.TIPCURCODIGO)


class ciudades(models.Model):
    CIUCODIGO=models.IntegerField(max_length=6, primary_key=True)
    CIUNOMBRE=models.CharField(max_length=20)

    
    def __str__(self):  
        return str(self.CIUCODIGO)

    
class sucursales(models.Model):
    SUCCODIGO=models.IntegerField(max_length=6, primary_key=True)
    CIUCODIGO=models.ForeignKey(ciudades, on_delete=models.CASCADE, default=1)
    SUCNOMBRE=models.CharField(max_length=20)

    def __str__(self):  
        return str(self.SUCCODIGO)

class matriculas(models.Model):
    MATNUMERO=models.IntegerField(max_length=11, primary_key=True, default=1)
    TIPCURCODIGO=models.ForeignKey(tipo_cursos,on_delete=models.CASCADE, default=1)
    ALUMRUT=models.ForeignKey(alumnos, on_delete=models.CASCADE, default=1)
    SUCCODIGO=models.ForeignKey(sucursales,on_delete=models.CASCADE, default=1)
    MATFECHA=models.DateField(default=timezone.now)

    def __str__(self):  
       return str( self.MATNUMERO)


    # matricula.TIPCURCODIGO.TIPCURNOMBRE

class usuarios(models.Model):
    USULOGIN=models.CharField(max_length=15, primary_key=True, default=1)
    USUPASSWORD=models.CharField(max_length=15)
