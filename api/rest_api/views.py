#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_braces.mixins import MultipleSerializersViewMixin

from django.db.models import Q

from .models import campaigns
from .serializers import campaigns_serializer, display_stands_serializer


class get_campaign(mixins.RetrieveModelMixin, generics.GenericAPIView):
	queryset = campaigns.objects.all()
	serializer_class = campaigns_serializer

	def get(self, request, *args, **kwargs):
		pk = kwargs.pop('pk', None)
		if not pk:
			serializer = campaigns_serializer(campaigns.objects.all(), many=True)
			return Response(serializer.data)
		return self.retrieve(request, *args, **kwargs)

class set_campaign(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = campaigns.objects.all()
	serializer_class = campaigns_serializer

	def put(self, request, *args, **kwargs):
		if self.create(request, *args, **kwargs):
			return Response({'result': 'success'}, status=status.HTTP_201_CREATED)

		return Response({'result': 'error'}, status=status.HTTP_400_BAD_REQUEST)