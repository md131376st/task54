"""task5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from task4.views import CsvView
from task4.views import some_view,static_page
from task4 import views
from django.conf.urls import url
# from page.views import ProfileImageView
from page.views import model_form_upload
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',model_form_upload, name='simple_upload'),
    url(r'csvfile/$', some_view, name='csvfile'),
    url(r'^(?P<page_alias>.+?)/$', static_page),


    # Project url patterns...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
