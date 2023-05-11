from django.contrib import admin
from .models import Aircraft
from accounts.models import Engineer
# Register your models here.

admin.site.register(Aircraft)
#admin.site.register(Engineer)