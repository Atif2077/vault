from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Chats)
admin.site.register(Person)
admin.site.register(Books)

# Register your models here.
