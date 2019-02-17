#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User

from django.utils.translation import ugettext as _

from .models import *

class display_stands_inline(admin.TabularInline):
	model = campaigns.display_stands.through
	extra = 1

	# fieldsets = (
	# 	('Rotation', {'fields': [('name', )]}),
	# 	# ('Products', {'fields': [('rotation_x', 'rotation_y', 'rotation_z', )]}),
	# )

class products_inline(admin.TabularInline):
	model = display_stands.products.through
	extra = 1

	fields = ['name', ]

class campaigns_admin(admin.ModelAdmin):
	inlines = [display_stands_inline, ]
	exclude = ('display_stands', )

	list_display = (
		'company', 'title', 'created_at', 'updated_at'
	)
	list_display_links = list_display

	list_filter = (
		'company', 'title',
	)

	fieldsets = (
		('Base', {'fields': ['company', 'title', ]}),
		('Position', {'fields': [('position_x', 'position_y', 'position_z', )]}),
		('Rotation', {'fields': [('rotation_x', 'rotation_y', 'rotation_z', )]}),
	)

	readonly_fields = ('updated_at', 'created_at', )

class display_stands_admin(admin.ModelAdmin):
	inline = [products_inline, ]
	exclude = ('products_inline', )

	list_display = (
		'name', 'type', 'created_at', 'updated_at'
	)
	list_display_links = list_display

	list_filter = (
		'name', 'type',
	)

	fieldsets = (
		('Base', {'fields': ['name', 'type', ]}),
		('Position', {'fields': [('position_x', 'position_y', 'position_z', )]}),
		('Rotation', {'fields': [('rotation_x', 'rotation_y', 'rotation_z', )]}),
		('Information', {'fields': ('scale', 'format', 'click_event', 'animation', )}),
		('Information', {'fields': ('products', )}),
	)

	readonly_fields = ('updated_at', 'created_at', )

class products_admin(admin.ModelAdmin):
	list_display = (
		'name', 'type', 'created_at', 'updated_at'
	)
	list_display_links = list_display

	list_filter = (
		'name', 'type',
	)

	fieldsets = (
		('Base', {'fields': ['name', 'type', ]}),
		('Position', {'fields': [('position_x', 'position_y', 'position_z', )]}),
		('Rotation', {'fields': [('rotation_x', 'rotation_y', 'rotation_z', )]}),
		('Information', {'fields': ('scale', 'format', 'click_event', 'animation', )}),
	)

	readonly_fields = ('updated_at', 'created_at', )

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(campaigns, campaigns_admin)
admin.site.register(display_stands, display_stands_admin)
admin.site.register(products, products_admin)