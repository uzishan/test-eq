from django.contrib import admin

from core.models import Building, Floor, Room, Sensor, SensorData



class BuildingAdmin(admin.ModelAdmin):
    pass

bModels = [models.Building, models.Floor, models.Room, models.Sensor, models.SensorData]
admin.site.register(bModels)
