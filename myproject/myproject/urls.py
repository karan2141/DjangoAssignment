from django.contrib import admin
from django.urls import path
from . import views
from .views import home
from accounts.views import oauth, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('oauth/', oauth, name="login"),
    path('register/', register_view, name ="register"),
    path('logout/', logout_view),
]
