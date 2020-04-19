from django.contrib import admin

from .models import Marks

class MarksAdmin(admin.ModelAdmin):
    fields = ['mark_user', 'title', 'describe', 'url']

admin.site.register(Marks, MarksAdmin)