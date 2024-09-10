from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken import views as token_view

router = DefaultRouter()

router.register("user_register", views.UserRegisterView, basename="Register")
router.register("profile", views.UserProfileView, basename="user_profile")
router.register("posts", views.PostView, basename="post_view")

urlpatterns = [
    path("social/token", token_view.obtain_auth_token),
] + router.urls
