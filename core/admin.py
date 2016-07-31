from django.contrib import admin

from core.models import Building, Floor, Room, Sensor, SensorData


class SensorDataAdmin(admin.ModelAdmin):
    model = SensorData


class SensorInline(admin.TabularInline):
    model = Sensor


class SensorAdmin(admin.ModelAdmin):
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
    inlines = [FloorInline]
    pass


admin.site.register(Building, BuildingAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorData, SensorDataAdmin)
