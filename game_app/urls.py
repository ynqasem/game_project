from django.urls import path
from game_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', views.game_create, name='create'),
    path('update/', views.game_update, name='update'),
    path('delete/', views.game_delete, name='delete'),
    path('list/', views.game_list, name='list'),
    path('detail/', views.game_detail, name='detail'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
