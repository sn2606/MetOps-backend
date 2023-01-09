from django.contrib import admin

from query.models import MetQuery, QueryForUser
from records.models import Record, RecordForQuery

# Register your models here.
admin.site.register(MetQuery)
admin.site.register(QueryForUser)
admin.site.register(Record)
admin.site.register(RecordForQuery)
