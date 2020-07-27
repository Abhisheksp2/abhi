from django.contrib import admin
from testApp.models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','mail','message','phonenumber']


admin.site.register(Contact,ContactAdmin)
