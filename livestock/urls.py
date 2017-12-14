from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin
admin.site.site_header = 'Livestock Administration'
#admin.site.site_header = _('My project')
admin.site.index_title = ('Site information')

urlpatterns = [
    # Examples:
    # url(r'^$', 'livestock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('liveapp.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
