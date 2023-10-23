from django.contrib import admin
from .models import Place
from .models import Transport
from .models import Accommodation
from .models import ThingsList
from .models import Tour


admin.site.register(Place)
admin.site.register(Transport)
admin.site.register(Accommodation)
admin.site.register(ThingsList)
admin.site.register(Tour)
