from django.urls import path
from .views import detail_view, create_view, list_view, send_mail

app_name = 'sld'
urlpatterns = [
    path('goruntule/<id>', detail_view, name='detail'),
    # path('goruntule1/<id>', detailnew_view),
    path('olustur', create_view, name='create'),
    path('liste', list_view, name='list'),
    path('gonder/<id>', send_mail, name='send_mail')
]
