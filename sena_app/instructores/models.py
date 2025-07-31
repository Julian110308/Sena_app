from django.db import models

class Instructor(models.Model):
    tipo_documento_choices = [
        ('CC', 'Cedula de ciudadania'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cedula de extranjeria'),
        ('PAS', 'Pasaporte'),
    ]
    
    nivel_educativo_choice = [
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especialización'),
        ('MAE', 'Maestría'),
        ('DOC', 'Doctorado'),
    ]
    
    documento_identidad = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=3, choices=tipo_documento_choices, default='CC')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=50)
    direccion = models.TextField(null=True)
    nivel_educativo = models.CharField(max_length=3, choices=nivel_educativo_choice, default='MAE')
    especialidad = models.CharField(max_length=100)
    anos_experiencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.especialidad}'
    
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'