from django.conf import settings

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'makemit.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mailsignup/', include('makemit.mailsignup.urls')),
    url(r'^materials/', include('makemit.materials.urls')),
    url(r'^review2015/', 'makemit.views.review2015', name='review2015'),
    url(r'^register/', RedirectView.as_view(url='https://techx.wufoo.com/forms/s16hd3aw1520tyz/', permanent=False), name='register'),
    url(r'^codeofconduct/', 'makemit.views.codeofconduct', name='codeofconduct'),
    url(r'^dayof/', RedirectView.as_view(url='http://dayof.makemit.org', permanent=False), name='dayof')
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
