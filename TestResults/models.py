from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):

    class TitleChoices(models.TextChoices):
        MISTER = 'Mr.',_('Mister')
        MISS = 'Ms.',_('Miss')
        DOCTOR = 'Dr.',_('Doctor')
        PROFESSOR = 'Prof.',_('Professor')

    title = models.CharField(max_length=5 ,choices=TitleChoices.choices, default=TitleChoices.MISTER)

    def __str__(self):
        return f"{self.title} {self.username}"

class PhysicalProblem(models.Model):
    name = models.CharField(max_length=32,help_text="Name of the physical problem to solve")
    
class TestData(models.Model):
    name = models.CharField(max_length=32,help_text="Name of the physical problem to solve")
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    datafile = models.FileField(upload_to=f"Tests\\users")