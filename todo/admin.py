from django.contrib import admin

from .models import (List, Item)

class ListModelAdmin(admin.ModelAdmin):
    list_display = ["title", "todoAmount" ,  "createTime"]
    list_filter = ["createTime"]
    search_fields = ["title"]
    list_editable = ["todoAmount"]
    class Meta:
        model = List

admin.site.register(List, ListModelAdmin)
admin.site.register(Item)

# Register your models here.
