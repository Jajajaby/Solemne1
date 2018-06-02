from django.contrib import admin
from .models import Team, Player, Coach, Payroll
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'thumb',)

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.logo.url))


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'rut', 'age', 'height', 'weight', 'thumb', 'email',)

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'rut', 'age', 'email', 'nickname',)


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time',)
