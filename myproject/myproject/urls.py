from django.contrib import admin
from django.urls import path
from . import views
from .views import homepage
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name="homepage"),
    path('accounts/login/', login_view, name="login"),
    path('accounts/register/', register_view, name ="register"),
    path('accounts/logout/', logout_view),
]
