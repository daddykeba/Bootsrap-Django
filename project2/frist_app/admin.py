# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from frist_app.models import Topic, Webpage, AccessRecord

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

# Register your models here.
