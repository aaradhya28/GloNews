
# Register your models here.
from django.contrib import admin
from .models import News
from .models import Visitor


admin.site.register(News)
admin.site.register(Visitor)