from django.contrib import admin
from django.urls import include, path
from game_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game_app/', include('game_app.urls')),
]
