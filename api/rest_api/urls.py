#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'
__VERSION__ = 'v1'

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import api_campaigns

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^{0}/campaigns/$'.format(__VERSION__), api_campaigns.as_view(), name='api_campaigns'),
	url(r'^{0}/campaigns/(?P<pk>[\d\-]+)/$'.format(__VERSION__), api_campaigns.as_view(), name='api_pk_campaigns'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
