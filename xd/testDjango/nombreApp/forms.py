from django import forms
from .models import contacto, Producto
from django.contrib.auth.forms import	UserCreationForm

class ContactoForm(forms.ModelForm):

  class Meta:
    model = contacto
    #fields= ["nombre","correo","tipo_consulta","mensaje","avisos"]
    fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
          "fecha_vencimiento": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm): 
  pass        