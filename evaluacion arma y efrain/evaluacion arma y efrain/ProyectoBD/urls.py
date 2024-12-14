"""
URL configuration for ProyectoBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appBD import views

urlpatterns = [
    path('',views.login_view),
    path('admin/', admin.site.urls),
    
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    
    path('alumnos/', views.Index_Alumnos, name='alumnos'),
    path('create-alumnos/',views.Create_Alumnos),
    path('view-alumnos/<str:id>/',views.View_Alumnos),
    path('update-alumnos/<str:id>/',views.Update_Alumnos),
    path('delete-alumnos/<str:id>/',views.Delete_Alumnos),
    path('filter-alumnos/',views.Filter_Alumnos),
    
    path('Cursos/',views.Index_TipoCursos),
    path('create-Cursos/',views.Create_TipoCursos),
    path('view-Cursos/<int:id>',views.View_TipoCursos),
    path('update-Cursos/<int:id>',views.Update_TipoCursos), 
    path('delete-Cursos/<int:id>',views.Delete_TipoCursos), 
    path('filter-Cursos/',views.Filter_Curso),
    

    path('Sucursales/',views.Index_Sucursales),
    path('create-Sucursales/',views.Create_Sucursales),
    path('view-Sucursales/<int:id>',views.View_Sucursales),
    path('update-Sucursales/<int:id>',views.Update_Sucursales), 
    path('delete-Sucursales/<int:id>',views.Delete_Sucursales),
    path('filter-Sucursales/',views.Filter_Sucursales),
        
    path('ciudades/',views.Index_Ciudades),
    path('create-ciudades/',views.Create_Ciudades),
    path('view-ciudades/<int:id>',views.View_Ciudades),
    path('update-ciudades/<int:id>',views.Update_Ciudades), 
    path('delete-ciudades/<int:id>',views.Delete_Ciudades),
    path('filter-ciudades/',views.Filter_Ciudades),

    path('usuarios/',views.Index_Usuarios),
    path('create-usuarios/',views.Create_Usuarios),
    path('update-user/<str:id>/',views.Update_User),
    path('ver-usuario/<str:id>/',views.View_User),
    path('delete-user/<str:id>/',views.Delete_User),
    
    path('Matricula/',views.Index_Matricula),
    path('create-Matricula/',views.Create_Matricula),
    path('view-Matricula/<int:id>',views.View_Matricula),
    path('update-Matricula/<int:id>',views.Update_Matricula), 
    path('delete-Matricula/<int:id>',views.Delete_Matricula), 
    path('filter-Matricula/',views.Filter_Matriculas),
    
    path('consultar_matriculas/', views.consultar_matriculas, name='consultar_matriculas'),
    path('consultar_matriculas_sucursal/', views.consultar_matriculas_por_sucursal, name='consultar_matriculas_sucursal'),
    path('consultar_alumnos/', views.consultar_alumnos, name='consultar_alumnos'),


    
    
]
