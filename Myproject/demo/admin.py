from django.contrib import admin
from .models import Menus, Events, MenuList, Message
# Register your models here.

admin.site.register(Menus)
admin.site.register(Events)
admin.site.register(MenuList)
admin.site.register(Message)