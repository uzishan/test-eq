from django.contrib import admin

from core.models import Building


class BuildingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Building, BuildingAdmin)
