"""getherprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import getherapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', getherapp.views.index, name='index'),
    path('base/', getherapp.views.base, name='base'), #나중에 base는 지울것
    path('feedback/', getherapp.views.feedback, name='feedback'),
    path('introduce/', getherapp.views.introduce, name='introduce'),
    path('sy_gwan/', getherapp.views.sy_gwan, name='sy_gwan'), # 1관 승연관
    path('im_gwan/', getherapp.views.im_gwan, name='im_gwan'), # 2관 일만관
    path('wd_gwan/', getherapp.views.wd_gwan, name='wd_gwan'), # 3관 월당관
    path('nn_gwan/', getherapp.views.nn_gwan, name='nn_gwan'), # 5관 나눔관
    path('jg_gwan/', getherapp.views.jg_gwan, name='jg_gwan'), # 6관 정보과학관
    path('scn_gwan/', getherapp.views.scn_gwan, name='scn_gwan'), # 7관 새천년관
    path('library/', getherapp.views.library, name='library'), # 8관 중앙도서관
    path('pb_hall/', getherapp.views.pb_hall, name='pb_hall'), # 9관 피츠버그홀
    path('gdin_gwan', getherapp.views.gdin_gwan, name='gdin_gwan'), # 10관 구두인관
    path('sbdr_school/', getherapp.views.sbdr_school, name='sbdr_school'), # 11관 성베드로학교
    path('mgell_gwan/', getherapp.views.mgell_gwan, name='mgell_gwan'), # 12관 미가엘관
    path('dormitory/', getherapp.views.dormitory, name='dormitory'), # 13관 행복기숙사
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
