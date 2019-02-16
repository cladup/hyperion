#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django.db import models
from django.utils.translation import ugettext as _

class campaigns(models.Model):
	class Meta:
		verbose_name = 'Campaigns'
		verbose_name_plural = 'Campaigns'
		unique_together = ('company', 'title', )

	company = models.CharField(_('Company Name'), max_length=50, null=False, blank=False)
	title = models.CharField(_('Company Title'), max_length=100, null=False, blank=False)
	camera_position_x = models.DecimalField(_('Camera Position X'), max_digits=5, decimal_places=2)
	camera_position_y = models.DecimalField(_('Camera Position Y'), max_digits=5, decimal_places=2)
	camera_position_z = models.DecimalField(_('Camera Position Z'), max_digits=5, decimal_places=2)
	camera_rotation_x = models.DecimalField(_('Camera Rotation X'), max_digits=5, decimal_places=2)
	camera_rotation_y = models.DecimalField(_('Camera Rotation Y'), max_digits=5, decimal_places=2)
	camera_rotation_z = models.DecimalField(_('Camera Rotation Z'), max_digits=5, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class display_stands(models.Model):
	class Meta:
		verbose_name = 'Display Stands'
		verbose_name_plural = 'Display Stands'

	campaign_id = models.ForeignKey(campaigns, on_delete=models.CASCADE)
	name = models.CharField(_('Display Stands Name'), max_length=50, null=False, blank=False)
	type = models.CharField(_('Display Stands type'), max_length=20, null=False, blank=False)
	position_x = models.DecimalField(_('Display Stands Position X'), max_digits=5, decimal_places=2)
	position_y = models.DecimalField(_('Display Stands Position Y'), max_digits=5, decimal_places=2)
	position_z = models.DecimalField(_('Display Stands Position Z'), max_digits=5, decimal_places=2)
	rotation_x = models.DecimalField(_('Display Stands Rotation X'), max_digits=5, decimal_places=2)
	rotation_y = models.DecimalField(_('Display Stands Rotation Y'), max_digits=5, decimal_places=2)
	rotation_z = models.DecimalField(_('Display Stands Rotation Z'), max_digits=5, decimal_places=2)
	scale = models.DecimalField(_('Display Stands Scale'), max_digits=5, decimal_places=2)
	format = models.CharField(_('Display Stands Format'), max_length=20, null=False, blank=False)
	click_event = models.CharField(_('Display Stands Click Event'), max_length=20, null=False, blank=False)
	animation = models.CharField(_('Display Stands Animation'), max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class products(models.Model):
	class Meta:
		verbose_name = 'Products'
		verbose_name_plural = 'Products'

	compaign_id = models.ForeignKey(campaigns, on_delete=models.CASCADE)
	display_stands_id = models.ForeignKey(display_stands, on_delete=models.CASCADE)
	name = models.CharField(_('Product Name'), max_length=50, null=False, blank=False)
	type = models.CharField(_('Product type'), max_length=20, null=False, blank=False)
	position_x = models.DecimalField(_('Product Position X'), max_digits=5, decimal_places=2)
	position_y = models.DecimalField(_('Product Position Y'), max_digits=5, decimal_places=2)
	position_z = models.DecimalField(_('Product Position Z'), max_digits=5, decimal_places=2)
	rotation_x = models.DecimalField(_('Product Rotation X'), max_digits=5, decimal_places=2)
	rotation_y = models.DecimalField(_('Product Rotation Y'), max_digits=5, decimal_places=2)
	rotation_z = models.DecimalField(_('Product Rotation Z'), max_digits=5, decimal_places=2)
	scale = models.DecimalField(_('Product Scale'), max_digits=5, decimal_places=2)
	format = models.CharField(_('Product Format'), max_length=20, null=False, blank=False)
	click_event = models.CharField(_('Product Click Event'), max_length=20, null=False, blank=False)
	animation = models.CharField(_('Product Animation'), max_length=20, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)