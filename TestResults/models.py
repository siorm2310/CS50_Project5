from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
# Create your models here.


class User(AbstractUser):

    class TitleChoices(models.TextChoices):
        MISTER = 'Mr.', _('Mister')
        MISS = 'Ms.', _('Miss')
        DOCTOR = 'Dr.', _('Doctor')
        PROFESSOR = 'Prof.', _('Professor')

    title = models.CharField(
        max_length=5, choices=TitleChoices.choices, default=TitleChoices.MISTER)

    def set_username(self):
        self.username = f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.title} {self.username}"


class PhysicalProblem(models.Model):
    name = models.CharField(
        max_length=32, help_text="Name of the physical problem to solve")


class TestData(models.Model):
    name = models.CharField(
        max_length=32, help_text="Name of the physical problem to solve")
    user = models.ForeignKey(User, related_name="user",
                             on_delete=models.CASCADE)
    submit_date = models.DateTimeField(default=now())
    problem = models.ForeignKey(
        PhysicalProblem, related_name="Physical_problem", on_delete=models.CASCADE, default=None)
    datafile = models.FileField(upload_to=f"Tests\\users", blank=True)
