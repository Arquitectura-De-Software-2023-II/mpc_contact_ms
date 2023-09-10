from django.urls import path, include

urlpatterns = [
    path('', include('service_info_ms.urls'))
]
