from django.contrib import admin

# Register your models here.
from .models import Table

admin.site.register(Table)

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)