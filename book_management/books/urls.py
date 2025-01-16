from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path
from .views import average_price

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('books/average-price/<int:year>/', average_price),
]
