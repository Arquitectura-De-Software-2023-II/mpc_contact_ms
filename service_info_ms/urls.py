from rest_framework import routers
from .api import AtendanceTimeViewSet, DoctorViewSet, ReviewViewSet, ServiceViewSet

router = routers.DefaultRouter()

router.register('api/atendance-time', AtendanceTimeViewSet, 'atendance-time')
router.register('api/doctors', DoctorViewSet, 'doctors')
router.register('api/review', ReviewViewSet, 'review')
router.register('api/service', ServiceViewSet, 'service')

urlpatterns = router.urls