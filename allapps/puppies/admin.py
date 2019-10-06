from django.contrib import admin
from .models import Puppy


# Register your models here.
class PuppyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Puppy, PuppyAdmin)
