from django.contrib import admin

from main.models import *

class TopicQueryAdmin(admin.ModelAdmin):
    model = TopicQuery
    list_filter = ('instance_id', 'filter_id')

admin.site.register(TopicQuery, TopicQueryAdmin)