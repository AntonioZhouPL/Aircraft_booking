from django.contrib import admin
from .models import Employee, Admin, Engineer
#from reservation.models import Aircraft
# Register your models here.

admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(Engineer)
#admin.site.register(Aircraft)