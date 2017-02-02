from django.conf.urls import url
from .views import home_directory


urlpatterns = [
    url(r'^home$', home_directory, name='home_directory'),
]
