from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_view  # type: ignore

router = DefaultRouter()
router.register("blog", views.BlogModelViewsetView, basename="bloge_view")
router.register("user", views.UserRegisterView, basename="user_view")

urlpatterns = [
    path("token", token_view.obtain_auth_token),
] + router.urls
