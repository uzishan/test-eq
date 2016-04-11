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
    
class FloorAdmin(admin.ModelAdmin):
    inlines = [RoomInline]
    pass

class BuildingAdmin(admin.ModelAdmin):
    inlines = [FloorInline]
    pass


admin.site.register(Building, BuildingAdmin)
admin.site.register(Floor, F;pprAd,om)
