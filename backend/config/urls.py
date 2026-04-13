from django.contrib import admin
from django.urls import path, include
from apps.ngo.views import home, login_view, register_view, dashboard_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('login/', login_view),
    path('register/', register_view),
    path('dashboard/', dashboard_view),
    path('logout/', logout_view),

    path('api/ngo/', include('apps.ngo.urls')),
    path('api/users/', include('apps.users.urls')),
]