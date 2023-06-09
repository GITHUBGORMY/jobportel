from django.contrib import admin

from app import models

admin.site.register(models.Login),
admin.site.register(models.Preferences),
admin.site.register(models.Application),
admin.site.register(models.Skill),