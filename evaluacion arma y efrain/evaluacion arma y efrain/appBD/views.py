from django.shortcuts import render,redirect
from django.utils import timezone
from appBD.models import alumnos,tipo_cursos,matriculas,ciudades,sucursales,usuarios
from . import forms
from django.urls import reverse
from .forms import AlumnoForm,tipo_cursosForm,MatriculasForm, MatriculasFilterForm,SucursalesForm,SucursalesFilterForm, CiudadesForm, AlumnoFilterForm, CursoFilterForm, CiudadesFilterForm, ConsultaMatriculasForm, ConsultaMatriculasSucursalForm, ConsultaAlumnosForm, UsuariosForm
# Create your views here.

from django.contrib.auth import logout

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('/login/')

## Tabla: Alumnos
def Index_Alumnos(request):
    Alumnos=alumnos.objects.all()
    data={'Alumnos':Alumnos}
    return render(request,'alumnos-index.html',data)

def Create_Alumnos(request):
    Alumnos=alumnos()
    form=AlumnoForm()
    if request.method=='POST':
        form=AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Alumnos(request)
    data={'form':form,'titulo':'Agregar Alumno'}
    return render(request,'alumnos-create.html',data)
    
    
def View_Alumnos(request,id):
    Alumnos=alumnos.objects.get(ALUMRUT=id)
    data={'Alumnos':Alumnos}
    return render(request,'alumnos-view.html',data)

def Update_Alumnos(request,id):
    Alumnos=alumnos.objects.get(ALUMRUT=id)
    form=AlumnoForm(instance=Alumnos)
    if request.method=="POST":
        form=AlumnoForm(request.POST,instance=Alumnos)
        if form.is_valid():
            form.save()
        return Index_Alumnos(request)
    data={'form':form,'titulo':'Actualizar Alumnos'}
    return render(request,'alumnos-create.html',data)


def Delete_Alumnos(request,id):
    Alumnos=alumnos.objects.get(ALUMRUT=id)
    Alumnos.delete()
    return redirect("/alumnos")

#Fin Tabla: Alumnos  
    
## Tabla: tipocursos
def Index_TipoCursos(request):
    Cursos=tipo_cursos.objects.all()
    data={'Cursos':Cursos}
    return render(request,'Cursos-index.html',data)

def Create_TipoCursos(request):
    Cursos=tipo_cursos()
    form=tipo_cursosForm()
    if request.method=='POST':
        form=tipo_cursosForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_TipoCursos(request)
    data={'form':form,'titulo':'Agregar Cursos'}
    return render(request,'Cursos-create.html',data)
    
    
def View_TipoCursos(request,id):
    Cursos=tipo_cursos.object.get(TIPCURCODIGO=id)
    data={'Cursos':Cursos}
    return render(request,'Cursos-view.html',data)

def Update_TipoCursos(request,id):
    Cursos=tipo_cursos.objects.get(TIPCURCODIGO=id)
    form=tipo_cursosForm(instance=Cursos)
    if request.method=="POST":
        form=tipo_cursosForm(request.POST,instance=Cursos)
        if form.is_valid():
            form.save()
        return Index_TipoCursos(request)
    data={'form':form,'titulo':'Actualizar Cursos'}
    return render(request,'Cursos-create.html',data)


def Delete_TipoCursos(request,id):
    Cursos=tipo_cursos.objects.get(TIPCURCODIGO=id)
    Cursos.delete()
    return redirect("/Cursos")
#Fin Tabla: tipocursos  

## Tabla: matriculas  matriculas

def Index_Matricula(request):
    Matricula=matriculas.objects.all()
    Cursos=tipo_cursos.objects.all()
    
    total_valor = sum([mat.TIPCURCODIGO.TIPCURVALOR for mat in Matricula])
    total_cursos = Matricula.count()
    data={'Matricula':Matricula, 'total_valor': total_valor, 'total_cursos': total_cursos}
    return render(request,'Matricula-index.html',data)

def Create_Matricula(request):
    Matricula=matriculas()
    form=MatriculasForm()
    if request.method=='POST':
        form=MatriculasForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Matricula(request)
    data={'form':form,'titulo':'Agregar Matricula'}
    return render(request,'Matricula-create.html',data)
    
    
def View_Matricula(request,id):
    Matricula=matriculas.objects.get(MATNUMERO=id)
    Cursos=tipo_cursos.objects.all()
    
    data={'Matricula':Matricula}
    return render(request,'Matricula-view.html',data)

def Update_Matricula(request,id):
    Matricula=matriculas.objects.get(MATNUMERO=id)
    form=MatriculasForm(instance=Matricula)
    if request.method=="POST":
        form=MatriculasForm(request.POST,instance=Matricula)
        if form.is_valid():
            form.save()
        return Index_Matricula(request)
    data={'form':form,'titulo':'Actualizar Matricula'}
    return render(request,'Matricula-create.html',data)


def Delete_Matricula(request,id):
    Matricula=matriculas.objects.get(MATNUMERO=id)
    Matricula.delete()
    return redirect("/Matricula")

#Fin Tabla: matriculas 
 
## Tabla: sucursales

def Index_Sucursales(request):
    Sucursales=sucursales.objects.all()
    data={'Sucursales':Sucursales}
    return render(request,'Sucursales-index.html',data)

def Create_Sucursales(request):
    form=SucursalesForm()
    if request.method=='POST':
        form=SucursalesForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Sucursales(request)
    data={'form': form, 'titulo':'Agregar Sucursal'}
    return render(request, 'Sucursales-create.html', data)
    
    
def View_Sucursales(request,id):
    Sucursales=sucursales.objects.get(SUCCODIGO=id)
    data={'Sucursales':Sucursales}
    return render(request,'Sucursales-view.html',data)

def Update_Sucursales(request,id):
    Sucursales=sucursales.objects.get(SUCCODIGO=id)
    form=SucursalesForm(instance=Sucursales)
    if request.method=="POST":
        form=SucursalesForm(request.POST,instance=Sucursales)
        if form.is_valid():
            form.save()
        return Index_Sucursales(request)
    data={'form':form,'titulo':'Actualizar Sucursales'}
    return render(request,'Sucursales-create.html',data)


def Delete_Sucursales(request,id):
    Sucursales=sucursales.objects.get(SUCCODIGO=id)
    Sucursales.delete()
    return redirect("/Sucursales")


#Fin Tabla: sucursales  

## Tabla: ciudades

def Index_Ciudades(request):
    Ciudad=ciudades.objects.all()
    data={'Ciudad':Ciudad}
    return render(request,'Ciudad-index.html',data)

def Create_Ciudades(request):
    Ciudad=ciudades()
    form=CiudadesForm()
    if request.method=='POST':
        form=CiudadesForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Ciudades(request)
    data={'form':form,'titulo':'Agregar Ciudad'}
    return render(request,'Ciudad-create.html',data)
    
    
def View_Ciudades(request,id):
    Ciudad=ciudades.objects.get(CIUCODIGO=id)
    data={'Ciudad':Ciudad}
    return render(request,'Ciudad-view.html',data)

def Update_Ciudades(request,id):
    Ciudad=ciudades.objects.get(CIUCODIGO=id)
    form=CiudadesForm(instance=Ciudad)
    if request.method=="POST":
        form=CiudadesForm(request.POST,instance=Ciudad)
        if form.is_valid():
            form.save()
        return Index_Ciudades(request)
    data={'form':form,'titulo':'Actualizar Ciudad'}
    return render(request,'Ciudad-create.html',data)


def Delete_Ciudades(request,id):
    Ciudad=ciudades.objects.get(CIUCODIGO=id)
    Ciudad.delete()
    return redirect("/ciudades")

#Fin Tabla: ciudades  

## Tabla: usuarios usuarios

#Fin Tabla: usuarios  

## Filtro de Alumnos

def Filter_Alumnos(request):
    form=AlumnoFilterForm()
    Alumnos=alumnos.objects.all()
    alumnosdata=request.GET

    if alumnosdata.get('ALUMRUT'):
        Alumnos = Alumnos.filter(ALUMRUT__icontains=alumnosdata.get('ALUMRUT'))
    if alumnosdata.get('ALUMAPATERNO'):
        Alumnos = Alumnos.filter(ALUMAPATERNO__icontains=alumnosdata.get('ALUMAPATERNO'))
    if alumnosdata.get('ALUMAMATERNO'):
        Alumnos = Alumnos.filter(ALUMAMATERNO__icontains=alumnosdata.get('ALUMAMATERNO'))
    if alumnosdata.get('ALUMDIRECCION'):
        Alumnos = Alumnos.filter(ALUMDIRECCION__icontains=alumnosdata.get('ALUMDIRECCION'))
    if alumnosdata.get('ALUMEMAIL'):
        Alumnos = Alumnos.filter(ALUMEMAIL__icontains=alumnosdata.get('ALUMEMAIL'))
    if alumnosdata.get('ALUMNFONO'):
        Alumnos = Alumnos.filter(ALUMNFONO__icontains=alumnosdata.get('ALUMNFONO'))

    data={'form':form, 'Alumnos': Alumnos}
    return render(request,'alumnos-filtro.html',data)
## Fin de  Filtro de Alumnos

def Filter_Curso(request):
    form=CursoFilterForm()
    Cursos=tipo_cursos.objects.all()
    Cursodata=request.GET

    if Cursodata.get('TIPCURCODIGO'):
        Cursos = Cursos.filter(TIPCURCODIGO__icontains=Cursodata.get('TIPCURCODIGO'))
    if Cursodata.get('TIPCURNOMBRE'):
        Cursos = Cursos.filter(TIPCURNOMBRE__icontains=Cursodata.get('TIPCURNOMBRE'))
    if Cursodata.get('TIPCURVALOR'):
        Cursos = Cursos.filter(TIPCURVALOR__icontains=Cursodata.get('TIPCURVALOR'))

    data={'form':form, 'Cursos': Cursos}
    return render(request,'Cursos-filtro.html',data)

def Filter_Ciudades(request):
    form=CiudadesFilterForm()
    Ciudad=ciudades.objects.all()
    Ciudadata=request.GET

    if Ciudadata.get('CIUCODIGO'):
        Ciudad = Ciudad.filter(CIUCODIGO__icontains=Ciudadata.get('CIUCODIGO'))
    if Ciudadata.get('CIUNOMBRE'):
        Ciudad = Ciudad.filter(CIUNOMBRE__icontains=Ciudadata.get('CIUNOMBRE'))

    data={'form':form, 'Ciudad': Ciudad}
    return render(request,'Ciudad-filtro.html',data)

def Filter_Sucursales(request):
    form=SucursalesFilterForm()
    Sucursales=sucursales.objects.all()
    Sucursalesdata=request.GET

    if Sucursalesdata.get('SUCCODIGO'):
        Sucursales = Sucursales.filter(SUCCODIGO__icontains=Sucursalesdata.get('SUCCODIGO'))
    if request.GET.get('CIUCODIGO'):
        Sucursales = Sucursales.filter(CIUCODIGO=request.GET.get('CIUCODIGO'))  
    if Sucursalesdata.get('SUCNOMBRE'):
        Sucursales = Sucursales.filter(SUCNOMBRE__icontains=Sucursalesdata.get('SUCNOMBRE'))

    data={'form':form, 'Sucursales': Sucursales}
    return render(request,'Sucursales-filtro.html',data)

def Filter_Matriculas(request):
    form=MatriculasFilterForm()
    Matricula=matriculas.objects.all()
    Matriculadata=request.GET

    if Matriculadata.get('MATNUMERO'):
        Matricula = Matricula.filter(MATNUMERO__icontains=Matriculadata.get('MATNUMERO'))
    if request.GET.get('TIPCURCODIGO'):
        Matricula = Matricula.filter(TIPCURCODIGO=request.GET.get('TIPCURCODIGO'))
        
    if request.GET.get('TIPCURNOMBRE'):
        Matricula = Matricula.filter(TIPCURNOMBRE=request.GET.get('TIPCURNOMBRE'))
        
    if request.GET.get('ALUMRUT'):
        Matricula = Matricula.filter(ALUMRUT=request.GET.get('ALUMRUT'))
        
    if request.GET.get('SUCCODIGO'):
        Matricula = Matricula.filter(SUCCODIGO=request.GET.get('SUCCODIGO'))
    
    if Matriculadata.get('MATFECHA'):
        Matricula = Matricula.filter(MATFECHA__icontains=Matriculadata.get('MATFECHA'))
        
    total_valor = sum([mat.TIPCURCODIGO.TIPCURVALOR for mat in Matricula])
    total_cursos = Matricula.count()

    data={'form':form, 'Matricula': Matricula, 'total_valor': total_valor, 'total_cursos': total_cursos}
    return render(request,'Matricula-filtro.html',data)

def consultar_matriculas(request):
    resultados = None
    total_valor = 0
    total_cursos = 0

    if request.method == 'POST':
        form = ConsultaMatriculasForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            resultados = matriculas.objects.filter(MATFECHA__range=[fecha_inicio, fecha_fin])
            total_valor = sum([mat.TIPCURCODIGO.TIPCURVALOR for mat in resultados])
            total_cursos = resultados.count()
    else:
        form = ConsultaMatriculasForm()

    return render(request, 'consultar_matriculas.html', {
        'form': form,
        'resultados': resultados,
        'total_valor': total_valor,
        'total_cursos': total_cursos,
    })


def consultar_matriculas_por_sucursal(request):
    resultados = None
    total_valor = 0
    total_cursos = 0
    Matricula = matriculas.objects.all()

    if request.method == 'POST':
        form = ConsultaMatriculasSucursalForm(request.POST)
        if form.is_valid():
            sucursal_seleccionada = form.cleaned_data['sucursal']
            resultados = matriculas.objects.filter(SUCCODIGO=sucursal_seleccionada)
            total_valor = sum([mat.TIPCURCODIGO.TIPCURVALOR for mat in resultados])
            total_cursos = resultados.count()
    else:
        form = ConsultaMatriculasSucursalForm()

    return render(request, 'consultar_matriculas_sucursal.html', {
        'form': form,
        'resultados': resultados,
        'total_valor': total_valor,
        'total_cursos': total_cursos,
    })


def consultar_alumnos(request):
    resultados = None
    if request.method == 'POST':
        form = ConsultaAlumnosForm(request.POST)
        if form.is_valid():
            filtros = {}
            if form.cleaned_data['rut']:
                filtros['ALUMRUT__icontains'] = form.cleaned_data['rut']
            if form.cleaned_data['nombre']:
                filtros['ALUMNOMBRE__icontains'] = form.cleaned_data['nombre']
            if form.cleaned_data['apellido_paterno']:
                filtros['ALUMAPATERNO__icontains'] = form.cleaned_data['apellido_paterno']
            if form.cleaned_data['apellido_materno']:
                filtros['ALUMAMATERNO__icontains'] = form.cleaned_data['apellido_materno']
            
            resultados = alumnos.objects.filter(**filtros)
    else:
        form = ConsultaAlumnosForm()

    return render(request, 'consultar_alumnos.html', {'form': form, 'resultados': resultados})

def Index_Usuarios(request):
    Usuarios=usuarios.objects.all()
    data={'usuarios': Usuarios}
    return render(request,'usuario-index.html',data)

def Create_Usuarios(request):
    form=UsuariosForm()
    if request.method=='POST':
        form=UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Usuarios(request)
    data={'form':form,'titulo':'Agregar Usuario'}
    return render(request,'usuario-create.html',data)

def View_User(request,id):
    Usuarios=usuarios.objects.get(USULOGIN=id)
    data={'Usuarios':Usuarios}
    return render(request,'user-view.html',data)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('USULOGIN')
        password = request.POST.get('USUPASSWORD')
        try:
            user = usuarios.objects.get(USULOGIN=username, USUPASSWORD=password)
            request.session['username'] = user.USULOGIN
            return redirect('alumnos') 
        except usuarios.DoesNotExist:
            error_message = "Usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def Delete_User(request,id):
    Usuarios=usuarios.objects.get(USULOGIN=id)
    Usuarios.delete()
    return redirect("/usuarios")

def Update_User(request,id):
    Usuarios=usuarios.objects.get(USULOGIN=id)
    form=UsuariosForm(instance=Usuarios)
    if request.method=="POST":
        form=UsuariosForm(request.POST,instance=Usuarios)
        if form.is_valid():
            form.save()
        return Index_Usuarios(request)
    data={'form':form,'titulo':'Actualizar Usuarios'}
    return render(request,'usuario-create.html',data)
