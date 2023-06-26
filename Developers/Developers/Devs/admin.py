from django.contrib import admin

from Developers.Devs.models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass
