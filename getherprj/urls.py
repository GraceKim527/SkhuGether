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
    path('feedback_cp/', getherapp.views.feedback_cp, name='feedback_cp'),
    path('introduce/', getherapp.views.introduce, name='introduce'),
    path('dormitory/', getherapp.views.dormitory, name='dormitory'),
    path('gdin_gwan', getherapp.views.gdin_gwan, name='gdin_gwan'),
    path('im_gwan/', getherapp.views.im_gwan, name='im_gwan'),
    path('jg_gwan/', getherapp.views.jg_gwan, name='jg_gwan'),
    path('library/', getherapp.views.library, name='library'),
    path('mgell_gwan/', getherapp.views.mgell_gwan, name='mgell_gwan'),
    path('nn_gwan/', getherapp.views.nn_gwan, name='nn_gwan'),
    path('pb_hall/', getherapp.views.pb_hall, name='pb_hall'),
    path('sbdr_school/', getherapp.views.sbdr_school, name='sbdr_school'),
    path('scn_gwan/', getherapp.views.scn_gwan, name='scn_gwan'),
    path('sy_gwan/', getherapp.views.sy_gwan, name='sy_gwan'),
    path('wd_gwan/', getherapp.views.wd_gwan, name='wd_gwan'),
    path('classroom/<str:unit_id>/<str:id>/', getherapp.views.classroom, name='classroom'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
