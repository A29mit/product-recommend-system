from django.contrib import admin
from mysite.models import Contact,Location
#from django.contrib.gis.admin import OSMGeoAdmin


# Register your models here.

admin.site.register(Contact)
admin.site.register(Location)
