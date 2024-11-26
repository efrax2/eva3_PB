from django.shortcuts import render,redirect
from appBD.models import alumnos,tipo_cursos,matriculas,ciudades,sucursales,usuarios
from . import forms
from .forms import AlumnoForm,tipo_cursosForm,MatriculasForm,SucursalesForm, CiudadesForm
# Create your views here.

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
    Alumnos=alumnos.objects.get(id=id)
    data={'Alumnos':Alumnos}
    return render(request,'alumnos-view.html',data)

def Update_Alumnos(request,id):
    Alumnos=alumnos.objects.get(id=id)
    form=AlumnoForm(instance=Alumnos)
    if request.method=="POST":
        form=AlumnoForm(request.POST,instance=Alumnos)
        if form.is_valid():
            form.save()
        return Index_Alumnos(request)
    data={'form':form,'titulo':'Actualizar Alumnos'}
    return render(request,'alumnos-create.html',data)


def Delete_Alumnos(request,id):
    Alumnos=alumnos.objects.get(id=id)
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
    Cursos=tipo_cursos.object.get(id=id)
    data={'Cursos':Cursos}
    return render(request,'Cursos-view.html',data)

def Update_TipoCursos(request,id):
    Cursos=tipo_cursos.objects.get(id=id)
    form=tipo_cursosForm(instance=Cursos)
    if request.method=="POST":
        form=tipo_cursosForm(request.POST,instance=Cursos)
        if form.is_valid():
            form.save()
        return Index_TipoCursos(request)
    data={'form':form,'titulo':'Actualizar Cursos'}
    return render(request,'Cursos-create.html',data)


def Delete_TipoCursos(request,id):
    Cursos=tipo_cursos.objects.get(id=id)
    Cursos.delete()
    return redirect("/Cursos")
#Fin Tabla: tipocursos  

## Tabla: matriculas  matriculas

def Index_Matricula(request):
    Matricula=matriculas.objects.all()
    data={'Matricula':Matricula}
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
    Matricula=matriculas.object.get(id=id)
    data={'Matricula':Matricula}
    return render(request,'Matricula-view.html',data)

def Update_Matricula(request,id):
    Matricula=matriculas.objects.get(id=id)
    form=MatriculasForm(instance=Matricula)
    if request.method=="POST":
        form=MatriculasForm(request.POST,instance=Matricula)
        if form.is_valid():
            form.save()
        return Index_Matricula(request)
    data={'form':form,'titulo':'Actualizar Matricula'}
    return render(request,'Matricula-create.html',data)


def Delete_Matricula(request,id):
    Matricula=matriculas.objects.get(id=id)
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
    return render(request, 'Sucursales-create.html')
    
    
def View_Sucursales(request,id):
    Sucursales=sucursales.objects.get(id=id)
    data={'Sucursales':Sucursales}
    return render(request,'Sucursales-view.html',data)

def Update_Sucursales(request,id):
    Sucursales=sucursales.objects.get(id=id)
    form=SucursalesForm(instance=Sucursales)
    if request.method=="POST":
        form=SucursalesForm(request.POST,instance=Sucursales)
        if form.is_valid():
            form.save()
        return Index_Sucursales(request)
    data={'form':form,'titulo':'Actualizar Sucursales'}
    return render(request,'Sucursales-create.html',data)


def Delete_Sucursales(request,id):
    Sucursales=sucursales.objects.get(id=id)
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
    Ciudad=ciudades.objects.get(id=id)
    data={'Ciudad':Ciudad}
    return render(request,'Ciudad-view.html',data)

def Update_Ciudades(request,id):
    Ciudad=ciudades.objects.get(id=id)
    form=CiudadesForm(instance=Ciudad)
    if request.method=="POST":
        form=CiudadesForm(request.POST,instance=Ciudad)
        if form.is_valid():
            form.save()
        return Index_Ciudades(request)
    data={'form':form,'titulo':'Actualizar Ciudad'}
    return render(request,'Ciudad-create.html',data)


def Delete_Ciudades(request,id):
    Ciudad=ciudades.objects.get(id=id)
    Ciudad.delete()
    return redirect("/ciudades")

#Fin Tabla: ciudades  

## Tabla: usuarios usuarios

#Fin Tabla: usuarios  