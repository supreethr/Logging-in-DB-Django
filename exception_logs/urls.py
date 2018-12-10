from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.exception_view, name='exception_view'),
]
