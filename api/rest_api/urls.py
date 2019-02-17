#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_campaign, set_campaign

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^campaign/get/$', get_campaign.as_view(), name='api_get_campaign'),
	url(r'^campaign/get/(?P<pk>[\d\-]+)/$', get_campaign.as_view(), name='api_get_campaign_detail'),
	url(r'^campaign/set/$', set_campaign.as_view(), name='api_set_campaign'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
