from django.contrib import admin
from .models import Teacher, Student


admin.site.register([Student])

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone']
