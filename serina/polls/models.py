from django.db import models
#from django.utils import timezone
#MODELOS DE LA BASE DE DATOS.
# Create your models here.


class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    contrasena = models.CharField(max_length=40)
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    ci = models.CharField(max_length = 8)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ci = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField()
    email_usuario = models.ForeignKey( Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Informacion(models.Model):
    ci_doctor = models.CharField(max_length=8, primary_key=True)
    nombre_doctor = models.CharField(max_length=40)
    apellido_doctor = models.CharField(max_length=40)
    tlf = models.CharField(max_length=40)
    clinica = models.CharField(max_length=40)
    class Meta:
        unique_together = ("nombre_doctor","apellido_doctor")

class Cita(models.Model):
    fecha = models.DateField()
    nota = models.CharField(max_length=70)
    email_usuario = models.ForeignKey( Usuario, on_delete=models.CASCADE)
    ci_informacion = models.ForeignKey(Informacion, on_delete=models.CASCADE)

class Imagen(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    link = models.URLField(max_length=300)
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()

    class Meta:
        unique_together = ("id_cita","link")

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)

class Tratamiento(models.Model):
    continuo = models.BooleanField()
    fecha_recipe = models.DateField()
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)

    class Meta:
        ordering = [ '-fecha_recipe' ]


class TipoMedicamento(models.Model):
    nombre = models.CharField(max_length=60, primary_key = True)

class Dosis(models.Model):
    tipo = models.CharField(max_length=40, primary_key = True)

class Medicina(models.Model):
    nombre = models.CharField(max_length=40, primary_key=True)
    tipo_medicamento = models.ForeignKey(TipoMedicamento, on_delete=models.CASCADE)
    tipo_dosis = models.ForeignKey(Dosis, on_delete=models.CASCADE)

    class Meta:
        unique_together = ( "nombre" , "tipo_medicamento" )


class Indicacion(models.Model):
    nombre_medicina = models.ForeignKey(Medicina, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    diferencia_horas = models.CharField(max_length= 40)
    cantidad_dosis = models.CharField(max_length=60)

class Nota(models.Model):
    fecha = models.DateField(primary_key=True)
    observacion = models.CharField(max_length=140)
    id_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

class CitaCategoria(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("id_cita","id_categoria")

class TratamientoMedicina(models.Model):
    id_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    nombre_medicina = models.ForeignKey(Medicina, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("id_tratamiento","nombre_medicina")
