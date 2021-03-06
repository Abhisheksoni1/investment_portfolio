"""investment_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from portfolio import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^bar/$', views.bar, name='bar'),
    url(r'^$', views.home, name='home'),
    url(r'^admin_bar/$', views.admin_bar, name='admin_bar'),
    url(r'^admin_bar/(?P<id>\d+)$', views.admin_bar, name='admin_bar'),
    url(r'^bar/(?P<id>\d+)$', views.bar, name='bar'),
    url(r'^fund_data/$', views.fund_data, name='fund_data'),
    url(r'^fund_data/(?P<id>\d+)$', views.fund_data, name='fund_data'),

]
