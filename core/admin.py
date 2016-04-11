from django.contrib import admin

from core.models import Building, Floor, Room, Sensor, SensorData

class SensorDataInline(admin.TabularInline):
    model = SensorData

class SensorInline(admin.TabularInline):
    model = Sensor
    inlines = [SensorDataInline]

class RoomInline(admin.TabularInline):
    model = Room
    inlines = [SensorInline]

class FloorInline(admin.TabularInline):
    model = Floor
    inlines = [RoomInline]

class BuildingAdmin(admin.ModelAdmin):
    inlines = [FloorInline]
    pass

bModels = [models.Building, models.Floor, models.Room, models.Sensor, models.SensorData]
admin.site.register(bModels)
