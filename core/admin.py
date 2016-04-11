from django.contrib import admin

from core.models import Building, Floor, Room, Sensor, SensorData

class SensorDataInline(admin.TabularInline):
    model = SensorData
    
class SensorInline(admin.TabularInline):
    model = Sensor

class SensorAdmin(admin.ModelAdmin):
    inlines = [SensorDataInline]
    pass
class RoomInline(admin.TabularInline):
    model = Room   

class RoomAdmin(admin.ModelAdmin):
    inlines = [SensorInline]
    pass
class FloorInline(admin.TabularInline):
    model = Floor
    
class FloorAdmin(admin.ModelAdmin):
    inlines = [RoomInline]
    pass

class BuildingAdmin(admin.ModelAdmin):
    fields = ('title')
    inlines = [FloorInline]
    pass


admin.site.register(Building, BuildingAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Sensor, SensorAdmin)
