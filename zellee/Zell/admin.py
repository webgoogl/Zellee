from django.contrib import admin
from Zell.models import contact,contactus,query
# Register your models here.

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('id','number')

@admin.register(query)
class queryAdmin(admin.ModelAdmin):
    list_display=('id','contact','email','message')

@admin.register(contactus)
class contactUsAdmin(admin.ModelAdmin):
    list_display=('id','name','email','message')