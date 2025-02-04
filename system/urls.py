"""
URL configuration for system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from users.views import change_password

admin.site.site_header = "School Management admin"
admin.site.site_title = "School Management admin"
admin.site.index_title = "School Management administration"
admin.empty_value_display = "**Empty**"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path(
        "accounts/logout/",
        views.LogoutView.as_view(),
        name="logout",
        kwargs={"next_page": "/"},
    ),
    path(
        "accounts/password/reset/",
        views.PasswordResetView.as_view(),
        name="passwordreset",
    ),
    path("change-password/", change_password, name="change_password"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
