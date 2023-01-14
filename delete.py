from query.models import *
from records.models import *

MetQuery.objects.raw('DELETE FROM query_metquery')
QueryForUser.objects.raw('DELETE FROM query_queryforuser')
Record.objects.raw('DELETE FROM records_record')
RecordForQuery.objects.raw('DELETE FROM records_recordforquery')
