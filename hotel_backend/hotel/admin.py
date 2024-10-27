from django.contrib import admin

from hotel.models import Classification, Thing, Tag, User

admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Thing)
admin.site.register(User)

