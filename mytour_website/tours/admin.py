from django.contrib import admin
from .models import Place
from .models import Transport
from .models import Accommodation
from .models import Sightseeing
from .models import Day
from .models import ThingsList
from .models import MyTourUser
from .models import Tour


admin.site.register(Place)
admin.site.register(Transport)
admin.site.register(Accommodation)
admin.site.register(Sightseeing)
admin.site.register(Day)
admin.site.register(ThingsList)
admin.site.register(MyTourUser)
admin.site.register(Tour)
