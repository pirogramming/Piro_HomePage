from django.urls import path, include
from .views import *
app_name = 'apply'

urlpatterns = [
    path('main', main, name="main" ),
    path('application', apply, name="application"),
    path('applyconfirm', applyConfirm, name="applyconfirm"),
    path('result/<slug:cat>', resultConfirm, name="result"),
]