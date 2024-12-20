from django import forms 
from appBD.models import alumnos, tipo_cursos, matriculas, sucursales, ciudades, usuarios


class AlumnoFilterForm(forms.Form):
    ALUMRUT = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="RUT del Alumno"
    )
    ALUMNOMBRE = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Nombre del Alumno"
    )
    ALUMAPATERNO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Apellido Paterno del Alumno"
    )
    ALUMAMATERNO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Apellido Materno del Alumno"
    )
    ALUMDIRECCION = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Direccion del Alumno"
    )
    ALUMEMAIL = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Correo del Alumno"
    )
    ALUMNFONO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Telefono del Alumno"
    )


class AlumnoForm(forms.ModelForm):
    class Meta:
        model=alumnos
        fields='__all__'
    
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields['ALUMRUT'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ALUMNOMBRE'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ALUMAPATERNO'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ALUMAMATERNO'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ALUMDIRECCION'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ALUMEMAIL'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ALUMNFONO'].widget.attrs.update({'class' : 'form-control'})

        self.fields['ALUMRUT'].label = "RUT del Alumno"
        self.fields['ALUMNOMBRE'].label = "Nombre del Alumno"
        self.fields['ALUMAPATERNO'].label = "Apellido Paterno del Alumno"
        self.fields['ALUMAMATERNO'].label = "Apellido Materno del Alumno"
        self.fields['ALUMDIRECCION'].label = "Dirrecion del Alumno"
        self.fields['ALUMEMAIL'].label = "Correo del Alumno"
        self.fields['ALUMNFONO'].label = "Telefono del Alumno"




class tipo_cursosForm(forms.ModelForm):
    class Meta:
        model=tipo_cursos
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(tipo_cursosForm, self).__init__(*args, **kwargs)
        self.fields['TIPCURCODIGO'].widget.attrs.update({'class' : 'form-control'})
        self.fields['TIPCURNOMBRE'].widget.attrs.update({'class' : 'form-control'})
        self.fields['TIPCURVALOR'].widget.attrs.update({'class' : 'form-control'})


        self.fields['TIPCURCODIGO'].label = "Codigo del Curso"
        self.fields['TIPCURNOMBRE'].label = "Nombre del Curso"
        self.fields['TIPCURVALOR'].label = "Valor del Curso"

class CursoFilterForm(forms.Form):
    TIPCURCODIGO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Codigo del Curso"
    )
    TIPCURNOMBRE = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Nombre del Curso"
    )
    TIPCURVALOR = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Valor del Curso"
    )

class MatriculasForm(forms.ModelForm):
    class Meta:
        model=matriculas
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(MatriculasForm, self).__init__(*args, **kwargs)
        self.fields['MATNUMERO'].widget.attrs.update({'class' : 'form-control'})
        self.fields['TIPCURCODIGO'].widget.attrs.update({'class' : 'form-select'})
        self.fields['ALUMRUT'].widget.attrs.update({'class' : 'form-select'})
        self.fields['SUCCODIGO'].widget.attrs.update({'class' : 'form-select'})
        self.fields['MATFECHA'].widget.attrs.update({'class' : 'form-control'})


        self.fields['MATNUMERO'].label = "Numero de Matricula"
        self.fields['TIPCURCODIGO'].label = "Codigo del Curso"
        self.fields['ALUMRUT'].label = "Rut del Alumno"
        self.fields['SUCCODIGO'].label = "Codigo de la Sucursal"
        self.fields['MATFECHA'].label = "Fecha de Matricula"

class MatriculasFilterForm(forms.Form):
    MATNUMERO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Numero de Matricula"
    )
    TIPCURCODIGO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-select'}),
        label="Codigo del Curso"
    )
    ALUMRUT = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-select'}),
        label="Rut del Alumno"
    )
    SUCCODIGO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-select'}),
        label="Codigo de la Sucursal"
    )
    MATFECHA = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Fecha de Matricula"
    )


class SucursalesForm(forms.ModelForm):
    class Meta:
        model = sucursales
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SucursalesForm, self).__init__(*args, **kwargs)
        self.fields['SUCCODIGO'].widget.attrs.update({'class' : 'form-control'})
        self.fields['CIUCODIGO'].widget.attrs.update({'class' : 'form-select'})
        self.fields['SUCNOMBRE'].widget.attrs.update({'class' : 'form-control'})


        self.fields['SUCCODIGO'].label = "Codigo de Sucursal"
        self.fields['CIUCODIGO'].label = "Codigo de la Ciudad"
        self.fields['SUCNOMBRE'].label = "Nombre de la Sucursal"

class SucursalesFilterForm(forms.Form):
    SUCCODIGO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Codigo de Sucursal"
    )
    CIUCODIGO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-select'}),
        label="Codigo de la Ciudad"
    )
    SUCNOMBRE = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Nombre de la Sucursal"
    )



class CiudadesForm(forms.ModelForm):

    class Meta:
        model = ciudades
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CiudadesForm, self).__init__(*args, **kwargs)
        self.fields['CIUCODIGO'].widget.attrs.update({'class' : 'form-control'})
        self.fields['CIUNOMBRE'].widget.attrs.update({'class' : 'form-control'})


        self.fields['CIUCODIGO'].label = "Codigo de la Ciudad"
        self.fields['CIUNOMBRE'].label = "Nombre de la Ciudad"

class CiudadesFilterForm(forms.Form):
    CIUCODIGO = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Codigo de la Ciudad"
    )
    CIUNOMBRE = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Nombre de la Ciudad"
    )

