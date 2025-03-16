from django.contrib import admin
from .models import Param, SubParam, ServerParam

class ServerParamAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')
    search_fields = ('title',)

class SubParamAdmin(admin.ModelAdmin):
    list_display = ('title', 'param', 'created')
    search_fields = ('title',)

class ParamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

admin.site.register(Param, ParamAdmin)
admin.site.register(SubParam, SubParamAdmin)
admin.site.register(ServerParam, ServerParamAdmin)