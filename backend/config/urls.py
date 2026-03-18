from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/ngo/', include('apps.ngo.urls')),   # ✅ THIS LINE MUST BE THERE
]