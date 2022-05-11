from django.contrib import admin
from django.urls import path, include
from todo.views import RegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('auth/register', RegistrationView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/refresh-token', TokenRefreshView.as_view())
]