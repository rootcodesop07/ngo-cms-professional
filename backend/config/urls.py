from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from apps.ngo.views import home, login_view, dashboard
from apps.ngo.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ngo/', include('apps.ngo.urls')),
    path('api/users/', include('apps.users.urls')),
    path('', home),
    path('login/', login_view),
    path('dashboard/', dashboard),
]