#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import routers, serializers, viewsets, generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from .models import campaigns
from .serializers import campaigns_serializer, display_stands_serializer


class api_campaigns(
		mixins.ListModelMixin,
		mixins.CreateModelMixin,
		mixins.DestroyModelMixin,
		mixins.UpdateModelMixin,
		mixins.RetrieveModelMixin,
		generics.GenericAPIView):
	queryset = campaigns.objects.all()
	serializer_class = campaigns_serializer

	def get(self, request, *args, **kwargs):
		pk = kwargs.pop('pk', None)
		if not pk:
			serializer = campaigns_serializer(campaigns.objects.all(), many=True)
			return Response(serializer.data)
		return self.retrieve(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		created = self.create(request, *args, **kwargs)
		if created:
			return Response({'result': 'success', 'data': created.data}, status=status.HTTP_201_CREATED)

		return Response({'result': 'error'}, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, *args, **kwargs):
		updated = self.update(request, *args, **kwargs)
		if updated:
			return Response({'result': 'success', 'data': updated.data}, status=status.HTTP_200_OK)

		return Response({'result': 'error'}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		pk = kwargs.pop('pk', None)
		if not pk:
			return Response({'result': 'error'}, status=status.HTTP_404_NOT_FOUND)

		if self.destroy(request, *args, **kwargs):
			return Response({'result': 'success'}, status=status.HTTP_204_NO_CONTENT)

		return Response({'result': 'error'}, status=status.HTTP_400_BAD_REQUEST)