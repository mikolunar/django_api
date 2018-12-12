from django.contrib import admin

# Register your models here.

from . models import CV
from . models import Project
from . models import Location
from . models import Education
from . models import RawData
from users.models import Profile

admin.site.register(CV)
admin.site.register(Project)
admin.site.register(Location)
admin.site.register(Education)
admin.site.register(RawData)
admin.site.register(Profile)
