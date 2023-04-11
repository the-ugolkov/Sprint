from django.contrib import admin

from pereval.models import Users, PerevalAdded, Coords, PerevalImages, PerevalAreas

admin.site.register(Users)
admin.site.register(PerevalAdded)
admin.site.register(Coords)
admin.site.register(PerevalImages)
admin.site.register(PerevalAreas)
