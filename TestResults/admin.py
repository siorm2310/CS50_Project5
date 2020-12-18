from django.contrib import admin
from .models import User,PhysicalProblem,TestData
# Register your models here.

admin.site.register(PhysicalProblem)
admin.site.register(User)
admin.site.register(TestData)