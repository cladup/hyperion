#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from rest_framework import routers, serializers, viewsets
from .models import campaigns as Campaigns, display_stands as Display_Stands, products as Products
from collections import OrderedDict

class products_serializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = (
			'name', 'type',
			'position_x', 'position_y', 'position_z',
			'rotation_x', 'rotation_y', 'rotation_z',
			'scale', 'format', 'click_event', 'animation'
		)

class display_stands_serializer(serializers.ModelSerializer):
	products = products_serializer(many=True)

	class Meta:
		model = Display_Stands
		fields = (
			'name', 'type',
			'position_x', 'position_y', 'position_z',
			'rotation_x', 'rotation_y', 'rotation_z',
			'scale', 'format', 'click_event', 'animation',
			'products'
		)

class campaigns_serializer(serializers.ModelSerializer):
	display_stands = display_stands_serializer(many=True)

	class Meta:
		model = Campaigns
		fields = (
			'company', 'title',
			'position_x', 'position_y', 'position_z',
			'rotation_x', 'rotation_y', 'rotation_z',
			'display_stands'
		)

	def create(self, validated_data):
		dss = validated_data.pop('display_stands')
		
		c = Campaigns.objects.update_or_create(**validated_data)
		for ds in dss:
			d = Display_Stands.objects.update_or_create(
				name=ds['name'],
				type=ds['type'],
				position_x=ds['position_x'],
				position_y=ds['position_y'],
				position_z=ds['position_z'],
				rotation_x=ds['rotation_x'],
				rotation_y=ds['rotation_y'],
				rotation_z=ds['rotation_z'],
				scale=ds['scale'],
				format=ds['format'],
				click_event=ds['click_event'],
				animation=ds['animation'],
			)

			for ps in ds['products']:
				p = Products.objects.update_or_create(
					name=ds['name'],
					type=ds['type'],
					position_x=ds['position_x'],
					position_y=ds['position_y'],
					position_z=ds['position_z'],
					rotation_x=ds['rotation_x'],
					rotation_y=ds['rotation_y'],
					rotation_z=ds['rotation_z'],
					scale=ds['scale'],
					format=ds['format'],
					click_event=ds['click_event'],
					animation=ds['animation'],
				)
				p.save()
				d.products.add(p)

			d.save()
			c.display_stands.add(d)

		c.display_stands.add(d)
		c.save()
		return c