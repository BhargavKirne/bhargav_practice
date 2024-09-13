from django.contrib import admin
from .models import State, Place

class StateAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_filter = ('name')
    search_fields = ('name')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(State)
admin.site.register(Place)
