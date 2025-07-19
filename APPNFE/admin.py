from django.contrib import admin
from .models import *

class postAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'publish','create' , 'status')
    list_filter = ('status' , 'publish')
    search_fields = ['title' , 'des' , 'franceTitle' , 'franceDES']

admin.site.register(Post , postAdmin)


class contactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'phone' , 'email')
    search_fields = ['name' , 'phone' , 'message']


admin.site.register(ContactMessage ,contactAdmin )


admin.site.register(MyUser)
admin.site.register(Like)
