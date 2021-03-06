from django.db import models

# Create your models here.
class Car(models.Model):
#    id          =  models.AutoField()
    modelo      =  models.CharField(max_length = 20)
    placa       =  models.CharField(max_length = 7,unique= True)
    in_date     = models.DateTimeField(auto_now = True, null = True)
    out_date    = models.DateTimeField(null = True, default = None)
    presente    = models.BooleanField(default = True)


    def pagamento(self , delta):
        valor = delta.days * 24
        valor = valor + int(delta.seconds/3600)
        return valor


class Caixa(models.Model):
    cash        =  models.DecimalField(max_digits=5, decimal_places=2)
