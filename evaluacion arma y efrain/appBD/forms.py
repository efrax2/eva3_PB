from django import forms 
from appBD.models import alumnos, tipo_cursos, matriculas, sucursales, ciudades, usuarios

class AlumnoForm(forms.ModelForm):
    class Meta:
        model=alumnos
        fields='__all__'

class tipo_cursosForm(forms.ModelForm):
    class Meta:
        model=tipo_cursos
        fields='__all__'

class MatriculasForm(forms.ModelForm):
    class Meta:
        model=matriculas
        fields='__all__'

class SucursalesForm(forms.ModelForm):
    
    class Meta:
        model = sucursales
        fields = '__all__'

class CiudadesForm(forms.ModelForm):

    class Meta:
        model = ciudades
        fields = '__all__'