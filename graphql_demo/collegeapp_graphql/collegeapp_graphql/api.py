from rest_framework import routers
from collegeapp import views as my_views

# This module is used for manual insertion of data
#  from the endpoint, not needed in case  of json data loading
router = routers.DefaultRouter()
router.register(r'student', my_views.StudentViewSet)
router.register(r'university', my_views.UniversityViewSet)
