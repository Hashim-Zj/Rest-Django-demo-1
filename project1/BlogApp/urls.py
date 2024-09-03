from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("blog", views.BlogModelViewsetView, basename="bloge_view")
router.register("user", views.UserRegisterView, basename="user_view")

urlpatterns = [] + router.urls
