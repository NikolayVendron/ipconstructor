from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from .views import ReviewViewset, PageViewset, BuyerViewset, OrderViewset, SizeViewset, CoverViewset, PatternViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('order', OrderViewset, basename='order')
router.register('buyer', BuyerViewset, basename='buyer')
router.register('size', SizeViewset, basename='size')
router.register('cover', CoverViewset, basename='cover')
router.register('pattern', PatternViewset, basename='pattern')
router.register('review', ReviewViewset, basename='review')
router.register('page', PageViewset, basename='page')

urlpatterns = [
    url('', include(router.urls))
]