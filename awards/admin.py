from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('categories','colors')


# Register your models here.
admin.site.register(categories)
admin.site.register(colors)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Profile)
admin.site.register(Rating)
