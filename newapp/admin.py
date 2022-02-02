from django.contrib import admin
from .models import *

model_list = [VanbrodskiMotori]
admin.site.register(model_list)