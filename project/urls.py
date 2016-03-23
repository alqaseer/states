from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^state_list/$', 'main.views.state_list'),
    # url(r'^state_detail/(?P<id>.+)/$', 'main.views.state_detail'),
    url(r'^search_cities/$', 'main.views.search_cities'),
    url(r'^get_list/$', 'main.views.template_view'),
    url(r'^state_detail/(?P<name>.+)/$', 'main.views.detail_view'),


    url(r'^cbv_list/$' , views.StateListView.as_view()),
    url(r'^cbv_detail/(?P<pk>[0-9]+)/$', views.StateDetailView.as_view()),

    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^city_edit/(?P<pk>[0-9]+)/$', 'main.views.city_edit'),
    url(r'^city_delete/(?P<pk>[0-9]+)/$', 'main.views.city_delete'),
]
