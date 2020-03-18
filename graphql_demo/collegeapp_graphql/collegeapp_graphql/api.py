from rest_framework import routers
from collegeapp import views as my_views

router = routers.DefaultRouter()
router.register(r'student', my_views.StudentViewSet)
router.register(r'university', my_views.UniversityViewSet)