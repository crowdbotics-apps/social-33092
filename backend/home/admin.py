from django.contrib import admin
from .models import Login, Signup, Student, Teacher

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Signup)

# Register your models here.
