from django.contrib import admin
from .models import Grade

# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade_name', 'grade_number']
    search_fields = ('grade_name','grade_number')
    list_per_page = 10

# Register your models here.
admin.site.register(Grade, GradeAdmin)
