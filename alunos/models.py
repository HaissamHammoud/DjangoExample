from django.db import models

# Create your models here.
class Usuario(models.Model):
    matricula          =  models.AutoField(primary_keys = True)
    nome               =  models.CharField(max_lenght = 120)
    nascimento         =  models.DateField()

class Professor(models.Model.Usuario):







class Aluno(models.Model):
    matricula          =   models.AutoField(primary_keys = True)
    nome               =   models.CharField(max_length = 120)
    idade              =   models.IntegerField()
    COURSES_CHOICES    =   (
            ('1', 'violao'),
            ('2', 'guitarra'),
            ('3', 'canto'),
    )
    courses            =   models.CharField(
            max_lenght = 1,
            choices = COURSES_CHOICES,
            default = None,
    )
    email              =   models.EmailField(max_lenght = 254)
    activated          =   models.BooleanField(default = True)
