from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, label="Código del Programa", help_text="Ingrese el código único del programa.")
    nombre = forms.CharField(max_length=200, label="Nombre del Programa", help_text="Ingrese el nombre del programa.")
    nivel_formacion = forms.ChoiceField(choices=Programa.nivel_formacion_choice, label="Nivel de Formación", help_text="Seleccione el nivel de formación del programa.")
    modalidad = forms.ChoiceField(choices=Programa.modalidad_choice, label="Modalidad", initial='PRE', help_text="Seleccione la modalidad del programa.")
    duracion_meses = forms.IntegerField(min_value=1, label="Duración en Meses", help_text="Ingrese la duración del programa en meses.")
    duracion_horas = forms.IntegerField(min_value=1, label="Duración en Horas", help_text="Ingrese la duración del programa en horas.")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción del Programa", help_text="Ingrese una descripción detallada del programa.")
    competencias = forms.CharField(widget=forms.Textarea, label="Competencias a Desarrollar", help_text="Ingrese las competencias que se desarrollarán en el programa.")
    perfil_egreso = forms.CharField(widget=forms.Textarea, label="Perfil de Egreso", help_text="Ingrese el perfil de egreso del programa.")
    requisitos_ingreso = forms.CharField(widget=forms.Textarea, label="Requisitos de Ingreso", help_text="Ingrese los requisitos necesarios para ingresar al programa.")
    centro_formacion = forms.CharField(max_length=200, label="Centro de Formación", help_text="Ingrese el nombre del centro de formación donde se ofrece el programa.")
    regional = forms.CharField(max_length=100, label="Regional", help_text="Ingrese la regional a la que pertenece el programa.")
    estado = forms.ChoiceField(choices=Programa.estado_choice, initial='ACT', label="Estado", help_text="Seleccione el estado del programa.")
    fecha_creacion = forms.DateField(label="Fecha de Creación del Programa", help_text="Ingrese la fecha de creación del programa.")
    fecha_registro = forms.DateField(label="Fecha de Registro", help_text="Ingrese la fecha de registro del programa.")

    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')
        if not codigo or not nombre:
            raise forms.ValidationError("Los campos Código y Nombre son obligatorios.")
        return cleaned_data

    def save(self):
        """Método para guardar el programa en la base de datos"""
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                modalidad=self.cleaned_data['modalidad'],
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                descripcion=self.cleaned_data['descripcion'],
                competencias=self.cleaned_data['competencias'],
                perfil_egreso=self.cleaned_data['perfil_egreso'],
                requisitos_ingreso=self.cleaned_data['requisitos_ingreso'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data['fecha_registro']
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al guardar el programa: {str(e)}")
        