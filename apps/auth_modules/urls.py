from django.urls import path, include
from auth_modules.views import GoogleLogin, FacebookLogin
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path(
        "password_reset_confirm/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("accounts/", include("allauth.urls"), name="socialaccount_signup"),
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("facebook/", FacebookLogin.as_view(), name="facebook_login"),
]
