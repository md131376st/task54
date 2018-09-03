from django.shortcuts import render,Http404
from django.views.generic import DetailView
from django.views import generic
from page.models import CsvDoc
import pandas as pd
from django.http import HttpResponse
from django.template import Context, loader
from .tables import ListItemstable
from django_tables2 import SingleTableMixin
from django.views.generic.base import TemplateView
from page.models import CsvDoc
from collections import defaultdict
import dataStatistics.task as task
from django_tables2   import RequestConfig
# df= pd
name = dict()
for e in CsvDoc.objects.all():
    dd = defaultdict(list)
    name= pd.read_csv("media/" + e.csv_file.name)


def some_view(request):
    if request.method == 'GET':
        # name = pd.read_csv("media/" + e.csv_file.name)
        # print(name)
        # print(df.to_html)
        return render(request, 'csvfile.html', {'df':name})


def static_page(request, page_alias):  # page_alias holds the part of the url
    page_alias=page_alias.split('/')
    # print(name.columns)
    # print(page_alias[len(page_alias)-1])
    for e in name.columns:

        # print()
        if e == page_alias[len(page_alias)-1]:

            if (name[e].dtype == 'object'):
                print("hi")
                # print(name[e])
                return task.statistics_of_categorical_data(name[e])
            else:
                for each in name[e]:
                    if (each != 0 and each != 1):
                         isBool = False
                         break
                if isBool == True:
                    print("hi1")
                    return task.statistics_of_binary_data(name[e])

                else:
                    print("hi2")
                    return task.statistics_of_numerical_data(name[e])

    raise Http404("Page does not exist")

