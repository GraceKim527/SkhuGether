from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='lost_main'),
    path('write/', views.write, name='lost_write'),
    path('detail/<str:id>/', views.detail, name='lost_detail'),
    path('check_password/<str:id>/<str:page>/', views.check_password, name='check_password'),
    path('edit/<str:id>/', views.edit, name='lost_edit'),
    path('delete/<str:id>/', views.delete, name='lost_delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)