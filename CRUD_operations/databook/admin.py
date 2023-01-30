from django.contrib import admin
from databook.models import Cricketer

# Register your models here.
@admin.register(Cricketer)
class CricketerAdmin(admin.ModelAdmin):
    list_display=['id','name','country','jersey_no']