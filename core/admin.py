from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Work,Tags,Tools_used, Comment

admin.site.register(Work)
admin.site.register(Tags)
admin.site.register(Tools_used)
admin.site.register(Comment)