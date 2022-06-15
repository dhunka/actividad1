from django.urls import path 
from . import views
#primera ruta para  la aplicacion
urlpatterns=[
     path('plantilla',views.plantilla, name='plantilla'),
     path('Marca',views.Marcaa, name='marca'),
     path('agregar_producto', views.agregar_producto, name="agregar_producto"),
     path('listar_productos', views.listar_productos, name="listar_productos"),
     path('modificar_producto/<id>/', views.modificar_producto, name="modificar_producto"),
     path('eliminar_producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
     path('registro/',views.registro, name='registro'),
     path('mono',views.mono, name='mono'),
     path('pala',views.palaa, name='pala'),
     path('macetafea',views.macetafeaa, name='macetafea'),
     path('mace-negra',views.macenegraa, name='mace-negra'),
     path('rastrillo',views.rastrillo, name='rastrillo'),
     path('florosa',views.florosa, name='florosa'),
     path('tijerashoja',views.tijerashojaa, name='tijerashoja'),
     path('floramarillas',views.floramarillas, name='floramarillas'),
     path('tijerasbasicas',views.tijerasbasicass, name='tijerasbasicas'),
     path('macetarara',views.macetarara, name='macetarara'),
     path('bambu',views.bambu, name='bambu'),
     path('tierradehojas',views.tierradehojas, name='tierradehojas'),
     path('login',views.loginn, name='login'),


#     path('Producto',views.Producto, name='Producto')
          ]
# 127.0.0.1:8000/plantilla
# 127.0.0.1:8000/marca