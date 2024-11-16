from django.db import models

# Create your models here.

class comensal(models.Model):
    cedula = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class mesa(models.Model):
    num_mesa = models.AutoField(primary_key=True)
    capacidad = models.PositiveIntegerField()
    estado_mesa = models.CharField(max_length=20)

    def __str__(self):
        return f"mesa {self.num_mesa}"


class reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    cedula_comensal = models.ForeignKey(comensal, on_delete=models.CASCADE)
    num_mesa = models.ForeignKey(mesa, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    num_personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"reserva {self.id_reserva} - {self.cedula_comensal.nombre}"


class personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.PositiveIntegerField()
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class mesero(models.Model):
    id_mesero = models.AutoField(primary_key=True)
    id_personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    salario = models.PositiveIntegerField()
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"mesero: {self.id_personal.nombre}"


class cocinero(models.Model):
    id_cocinero = models.AutoField(primary_key=True)
    id_personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    salario = models.PositiveIntegerField()
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"cocinero: {self.id_personal.nombre}"


class menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_menu = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class plato(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_plato = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    id_menu = models.ForeignKey(menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class prepara(models.Model):
    id_plato = models.ForeignKey(plato, on_delete=models.CASCADE)
    id_cocinero = models.ForeignKey(cocinero, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_plato', 'id_cocinero')

    def __str__(self):
        return f"{self.id_cocinero.id_personal.nombre} prepara {self.id_plato.nombre}"


class ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_ingrediente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class ingredientes_plato(models.Model):
    id_ingrediente = models.ForeignKey(ingrediente, on_delete=models.CASCADE)
    id_plato = models.ForeignKey(plato, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_ingrediente', 'id_plato')

    def __str__(self):
        return f"{self.id_ingrediente.nombre} en {self.id_plato.nombre}"


class pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    ced_comensal = models.ForeignKey(comensal, on_delete=models.CASCADE)
    id_plato = models.ForeignKey(plato, on_delete=models.CASCADE)
    id_mesero = models.ForeignKey(mesero, on_delete=models.CASCADE)
    cantidad_platos = models.PositiveIntegerField()
    total_pago = models.PositiveIntegerField()

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.ced_comensal.nombre}"


class pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    pago_total = models.PositiveIntegerField()
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago {self.id_pago} - Pedido {self.id_pedido.id_pedido}"
