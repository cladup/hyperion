#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django.db.models import Q
from rest_framework import routers, serializers, viewsets

from .models import campaigns as Campaigns, display_stands as Display_Stands, products as Products

class products_serializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = (
			'id', 'name', 'type',
			'position_x', 'position_y', 'position_z',
			'rotation_x', 'rotation_y', 'rotation_z',
			'scale', 'format', 'click_event', 'animation'
		)

class display_stands_serializer(serializers.ModelSerializer):
	products = products_serializer(many=True)

	class Meta:
		model = Display_Stands
		fields = (
			'id', 'name', 'type',
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
			'id', 'company', 'title',
			'position_x', 'position_y', 'position_z',
			'rotation_x', 'rotation_y', 'rotation_z',
			'display_stands'
		)

	def create(self, validated_data):
		c_id = self.initial_data.get('id')
		dss = self.initial_data.get('display_stands')

		c = Campaigns.objects.create()
		c.company = self.initial_data.get('company')
		c.title = self.initial_data.get('title')
		c.position_x = self.initial_data.get('position_x')
		c.position_y = self.initial_data.get('position_y')
		c.position_z = self.initial_data.get('position_z')
		c.rotation_x = self.initial_data.get('rotation_x')
		c.rotation_y = self.initial_data.get('rotation_y')
		c.rotation_z = self.initial_data.get('rotation_z')

		for ds in dss:
			d = Display_Stands.objects.create()
			d.name = ds['name']
			d.type = ds['type']
			d.position_x = ds['position_x']
			d.position_y = ds['position_y']
			d.position_z = ds['position_z']
			d.rotation_x = ds['rotation_x']
			d.rotation_y = ds['rotation_y']
			d.rotation_z = ds['rotation_z']
			d.scale = ds['scale']
			d.format = ds['format']
			d.click_event = ds['click_event']
			d.animation = ds['animation']

			for ps in ds['products']:
				p = Products.objects.create()
				p.name = ps['name']
				p.type = ps['type']
				p.position_x = ps['position_x']
				p.position_y = ps['position_y']
				p.position_z = ps['position_z']
				p.rotation_x = ps['rotation_x']
				p.rotation_y = ps['rotation_y']
				p.rotation_z = ps['rotation_z']
				p.scale = ps['scale']
				p.format = ps['format']
				p.click_event = ps['click_event']
				p.animation = ps['animation']
				
				p.save()
				d.products.add(p)

			d.save()
			c.display_stands.add(d)

		c.save()
		return c

	def update(self, instance, validated_data):
		c_id = self.initial_data.get('id')
		dss = self.initial_data.get('display_stands')

		c = Campaigns.objects.filter(Q(id=instance.id))
		if c.exists():
			c = c.first()
		else:
			return None

		c.company = self.initial_data.get('company')
		c.title = self.initial_data.get('title')
		c.position_x = self.initial_data.get('position_x')
		c.position_y = self.initial_data.get('position_y')
		c.position_z = self.initial_data.get('position_z')
		c.rotation_x = self.initial_data.get('rotation_x')
		c.rotation_y = self.initial_data.get('rotation_y')
		c.rotation_z = self.initial_data.get('rotation_z')

		for ds in dss:
			d = None
			if ('id' in ds):
				d = c.display_stands.filter(Q(id=ds['id']))
				if d.exists():
					d = d.first()
				else:
					continue
			else:
				return None
			
			d.name = ds['name']
			d.type = ds['type']
			d.position_x = ds['position_x']
			d.position_y = ds['position_y']
			d.position_z = ds['position_z']
			d.rotation_x = ds['rotation_x']
			d.rotation_y = ds['rotation_y']
			d.rotation_z = ds['rotation_z']
			d.scale = ds['scale']
			d.format = ds['format']
			d.click_event = ds['click_event']
			d.animation = ds['animation']

			for ps in ds['products']:
				p = None
				if ('id' in ps):
					p = d.products.filter(Q(id=ps['id']))
					if p.exists():
						p = p.first()
					else:
						continue
				else:
					return None

				p.name = ps['name']
				p.type = ps['type']
				p.position_x = ps['position_x']
				p.position_y = ps['position_y']
				p.position_z = ps['position_z']
				p.rotation_x = ps['rotation_x']
				p.rotation_y = ps['rotation_y']
				p.rotation_z = ps['rotation_z']
				p.scale = ps['scale']
				p.format = ps['format']
				p.click_event = ps['click_event']
				p.animation = ps['animation']
				
				p.save()
				d.products.add(p)

			d.save()
			c.display_stands.add(d)

		c.save()
		return c