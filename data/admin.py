from django.contrib import admin
from .models import Data, Contact

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['sname','sroll','scourse','saddress']

class ConAdmin(admin.ModelAdmin):
    list_display = ['cname','cemail','cmessage']

admin.site.register(Data,DataAdmin)
admin.site.register(Contact,ConAdmin)



