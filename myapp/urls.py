from django.urls import path
from django.urls import path
# from .views import DataPointList

from django.urls import path
from .views import get_data, dashboard, visualization_page

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('visualization/', visualization_page, name='visualization'),
    path('api/data/', get_data, name='get_data'),
]



