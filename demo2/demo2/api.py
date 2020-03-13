from rest_framework import routers
from rental import views as myviews

router = routers.DefaultRouter()
router.register(r'student',myviews.StudentViewset)
router.register(r'library',myviews.LibraryViewset)
router.register(r'borrowed',myviews.BorrowedViewset)
