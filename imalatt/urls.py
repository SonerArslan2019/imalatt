from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include("imalatt.apps.home.urls", namespace='home')),
    path('sld/', include("imalatt.apps.sld.urls", namespace='sld')),
    path('user/', include("imalatt.apps.user.urls")),
    path('admin/', admin.site.urls),    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns