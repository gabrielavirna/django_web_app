from django.contrib import admin

# Import your model
from collection.models import Thing

# And register it here.
# admin.site.register(Thing)


# Set up an automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    # show up name and description in your admin
    list_display = ('name', 'description',)
    # pre populates the DB's field 'slug' with the thing's name
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Thing, ThingAdmin)


