import django_tables2 as tables
import pandas as pd
from page.models import CsvDoc

# we don't use the functions
def func():
    for e in CsvDoc.objects.all():
        items = pd.read_csv("media/"+e.csv_file.name).columns.values
    return items


class ListItemstable(tables.Table):
    class Meta:
        pass
        # fields = func()
        # model = CsvDoc
        # attrs = {'class': 'table'}
    pass




