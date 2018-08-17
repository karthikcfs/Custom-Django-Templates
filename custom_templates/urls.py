from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from myapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'custom_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^admin/', include(admin.site.urls)),
)
