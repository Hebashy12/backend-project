from django.contrib import admin
from .models import Destination
from .models import Doctors
from .models import RegisterUsers
from .models import Schedule
from .models import Appointment

# Register your models here.
admin.site.register(Destination)
admin.site.register(Doctors)
admin.site.register(RegisterUsers)
admin.site.register(Schedule)
admin.site.register(Appointment)
