from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactCustomization(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']


admin.site.register(Contact, ContactCustomization)

