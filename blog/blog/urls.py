from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from boletin import views
from .views import  about
from .views import  page
from .views import detalhes
from .views import lixo
from .views import solucoes



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contato, name='contact'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^about/$',about, name='about'),
    url(r'^page/$',page, name='page'),
    url(r'^detalhes/$',detalhes, name='detalhes'),
    url(r'^lixo/$',lixo, name='lixo'),
    url(r'^solucoes/$',solucoes, name='solucoes'),

    url(r'^accounts/', include('registration.backends.default.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

