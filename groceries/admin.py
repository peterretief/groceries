from django.contrib import admin

# Register your models here.
from .models import Unit
admin.site.register(Unit)
from .models import Vendor
admin.site.register(Vendor)
from .models import Item
admin.site.register(Item)
from .models import Buy
admin.site.register(Buy)
