
from django.urls import path
from .views import login_view,logout_view


app_name = "user"

urlpatterns = [
    path('giris/',login_view,name='login'),
    path('cikis/',logout_view,name="logout"),
]

