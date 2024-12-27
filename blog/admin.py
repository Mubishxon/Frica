from django.contrib import admin
from .models import Beauty, Customer, Free, Kiyimlar, Computer, Contact
# Register your models here.
admin.site.register(Beauty)
admin.site.register(Customer)
admin.site.register(Free)
admin.site.register(Kiyimlar)
admin.site.register(Contact)

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}