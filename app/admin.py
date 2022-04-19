from atexit import register
from django.contrib import admin
from app.models import FormModel
# Register your models here.
admin.site.register(FormModel)