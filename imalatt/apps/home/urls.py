from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', home_view, name='home'),
    path('kapilar/',kapilar_view,name='kapilar'),
    path('about_sld/', aboutsld_view, name='aboutsld'),
    path('401/', view_401,name='401'),
]