from django.contrib import admin

# Register your models here.

from .models import Skill, Job, Application

admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Application)
