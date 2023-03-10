from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.MeViewSet, basename='me')

urlpatterns = [] + router.urls

# urlpatterns = [
    # path('', views.MeViewSet.as_view({'get': 'list'}), name='me'),
# ]
