from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Publications)
admin.site.register(Tag)
admin.site.register(Reader)
admin.site.register(ReadList)