from rest_framework import routers
from .api import DoctorViewSet

router = routers.DefaultRouter()

router.register('api/atendance-time', DoctorViewSet, 'atendance-time')
router.register('api/doctors', DoctorViewSet, 'doctors')
router.register('api/review', DoctorViewSet, 'review')
router.register('api/service', DoctorViewSet, 'service')

urlpatterns = router.urls