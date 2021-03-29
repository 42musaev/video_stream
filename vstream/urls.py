from django.urls import path

from vstream.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index')
]