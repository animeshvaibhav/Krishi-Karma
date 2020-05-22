from django.contrib import admin
from krishiKarma.models import State,Crop,District,Farmer,Category,Soil

# Register your models here.

admin.site.register(State)
admin.site.register(District)
admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(Category)
admin.site.register(Soil)