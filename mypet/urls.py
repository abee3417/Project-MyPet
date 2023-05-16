from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'mypet'

urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
    path('daily/', views.daily, name='daily'),
    path('photo/', views.photo, name='photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
