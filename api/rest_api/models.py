#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by StolenByte
__AUTHOR__ = 'StolenByte [thscndgh@gmail.com]'

from django.db import models
from django.utils.translation import ugettext as _

'''
class campaigns(models.Model):
	class Meta:
		verbose_name = 'Campaigns'
		verbose_name_plural = 'Campaigns'
		unique_together = ('company', 'title', )

	company = models.CharField(_('Company Name'), max_length=50, null=False, blank=False, default='')
	title = models.CharField(_('Company Title'), max_length=100, null=False, blank=False, default='')
	position_x = models.DecimalField(_('Position X'), max_digits=5, decimal_places=2, default=0.0)
	position_y = models.DecimalField(_('Position Y'), max_digits=5, decimal_places=2, default=0.0)
	position_z = models.DecimalField(_('Position Z'), max_digits=5, decimal_places=2, default=0.0)
	rotation_x = models.DecimalField(_('Rotation X'), max_digits=5, decimal_places=2, default=0.0)
	rotation_y = models.DecimalField(_('Rotation Y'), max_digits=5, decimal_places=2, default=0.0)
	rotation_z = models.DecimalField(_('Rotation Z'), max_digits=5, decimal_places=2, default=0.0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s : %s' % (self.company, self.title)

	def to_dict(self):
		return {
			'company': self.company,
			'title': self.title,
			'position': {
				'x': self.position_x,
				'y': self.position_y,
				'z': self.position_z,
			},
			'rotation': {
				'x': self.rotation_x,
				'y': self.rotation_y,
				'z': self.rotation_z,
			},
		}

class display_stands(models.Model):
	class Meta:
		verbose_name = 'Display Stands'
		verbose_name_plural = 'Display Stands'

	campaign_id = models.ForeignKey(campaigns, verbose_name=_('Campaign ID'), on_delete=models.CASCADE, default=None)
	name = models.CharField(_('Display Stands Name'), max_length=50, null=False, blank=False, default='')
	type = models.CharField(_('Display Stands Type'), max_length=20, null=False, blank=False, default='')
	position_x = models.DecimalField(_('Display Stands Position X'), max_digits=5, decimal_places=2, default=0.0)
	position_y = models.DecimalField(_('Display Stands Position Y'), max_digits=5, decimal_places=2, default=0.0)
	position_z = models.DecimalField(_('Display Stands Position Z'), max_digits=5, decimal_places=2, default=0.0)
	rotation_x = models.DecimalField(_('Display Stands Rotation X'), max_digits=5, decimal_places=2, default=0.0)
	rotation_y = models.DecimalField(_('Display Stands Rotation Y'), max_digits=5, decimal_places=2, default=0.0)
	rotation_z = models.DecimalField(_('Display Stands Rotation Z'), max_digits=5, decimal_places=2, default=0.0)
	scale = models.DecimalField(_('Display Stands Scale'), max_digits=5, decimal_places=2, default=0.0)
	format = models.CharField(_('Display Stands Format'), max_length=20, null=False, blank=False, default='')
	click_event = models.CharField(_('Display Stands Click Event'), max_length=20, null=False, blank=False, default='')
	animation = models.CharField(_('Display Stands Animation'), max_length=20, null=False, blank=False, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s : %s' % (self.name, self.type)

	def to_dict(self):
		return {
			'name': self.name,
			'type': self.type,
			'position': {
				'x': self.position_x,
				'y': self.position_y,
				'z': self.position_z,
			},
			'rotation': {
				'x': self.rotation_x,
				'y': self.rotation_y,
				'z': self.rotation_z,
			},
			'scale': self.scale,
			'format': self.format,
			'click_event': self.click_event,
			'animation': self.animation,
		}

class products(models.Model):
	class Meta:
		verbose_name = 'Products'
		verbose_name_plural = 'Products'

	# campaign_id = models.ForeignKey(campaigns, verbose_name=_('Campaign ID'), on_delete=models.CASCADE, default=None)
	# display_stand_id = models.ForeignKey(display_stands, verbose_name=_('Display Stands ID'), on_delete=models.CASCADE, default=None)
	name = models.CharField(_('Product Name'), max_length=50, null=False, blank=False, default='')
	type = models.CharField(_('Product type'), max_length=20, null=False, blank=False, default='')
	position_x = models.DecimalField(_('Product Position X'), max_digits=5, decimal_places=2, default=0.0)
	position_y = models.DecimalField(_('Product Position Y'), max_digits=5, decimal_places=2, default=0.0)
	position_z = models.DecimalField(_('Product Position Z'), max_digits=5, decimal_places=2, default=0.0)
	rotation_x = models.DecimalField(_('Product Rotation X'), max_digits=5, decimal_places=2, default=0.0)
	rotation_y = models.DecimalField(_('Product Rotation Y'), max_digits=5, decimal_places=2, default=0.0)
	rotation_z = models.DecimalField(_('Product Rotation Z'), max_digits=5, decimal_places=2, default=0.0)
	scale = models.DecimalField(_('Product Scale'), max_digits=5, decimal_places=2, default=0.0)
	format = models.CharField(_('Product Format'), max_length=20, null=False, blank=False, default='')
	click_event = models.CharField(_('Product Click Event'), max_length=20, null=False, blank=False, default='')
	animation = models.CharField(_('Product Animation'), max_length=20, null=False, blank=False, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def to_dict(self):
		return {
			'name': self.name,
			'type': self.type,
			'position': {
				'x': self.position_x,
				'y': self.position_y,
				'z': self.position_z,
			},
			'rotation': {
				'x': self.rotation_x,
				'y': self.rotation_y,
				'z': self.rotation_z,
			},
			'scale': self.scale,
			'format': self.format,
			'click_event': self.click_event,
			'animation': self.animation,
		}
'''


class products(models.Model):
	class Meta:
		verbose_name = 'Products'
		verbose_name_plural = 'Products'

	name = models.CharField(_('Product Name'), max_length=50, null=False, blank=False, default='')
	type = models.CharField(_('Product type'), max_length=20, null=False, blank=False, default='')
	position_x = models.DecimalField(_('Product Position X'), max_digits=5, decimal_places=2, default=0.0)
	position_y = models.DecimalField(_('Product Position Y'), max_digits=5, decimal_places=2, default=0.0)
	position_z = models.DecimalField(_('Product Position Z'), max_digits=5, decimal_places=2, default=0.0)
	rotation_x = models.DecimalField(_('Product Rotation X'), max_digits=5, decimal_places=2, default=0.0)
	rotation_y = models.DecimalField(_('Product Rotation Y'), max_digits=5, decimal_places=2, default=0.0)
	rotation_z = models.DecimalField(_('Product Rotation Z'), max_digits=5, decimal_places=2, default=0.0)
	scale = models.DecimalField(_('Product Scale'), max_digits=5, decimal_places=2, default=0.0)
	format = models.CharField(_('Product Format'), max_length=20, null=False, blank=False, default='')
	click_event = models.CharField(_('Product Click Event'), max_length=20, null=False, blank=False, default='')
	animation = models.CharField(_('Product Animation'), max_length=20, null=False, blank=False, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s <%s>' % (self.name, self.type)

	def to_dict(self):
		return {
			'name': self.name,
			'type': self.type,
			'position': {
				'x': self.position_x,
				'y': self.position_y,
				'z': self.position_z,
			},
			'rotation': {
				'x': self.rotation_x,
				'y': self.rotation_y,
				'z': self.rotation_z,
			},
			'scale': self.scale,
			'format': self.format,
			'click_event': self.click_event,
			'animation': self.animation,
		}

class display_stands(models.Model):
	class Meta:
		verbose_name = 'Display Stands'
		verbose_name_plural = 'Display Stands'

	name = models.CharField(_('Display Stands Name'), max_length=50, null=False, blank=False, default='')
	type = models.CharField(_('Display Stands Type'), max_length=20, null=False, blank=False, default='')
	position_x = models.DecimalField(_('Display Stands Position X'), max_digits=5, decimal_places=2, default=0.0)
	position_y = models.DecimalField(_('Display Stands Position Y'), max_digits=5, decimal_places=2, default=0.0)
	position_z = models.DecimalField(_('Display Stands Position Z'), max_digits=5, decimal_places=2, default=0.0)
	rotation_x = models.DecimalField(_('Display Stands Rotation X'), max_digits=5, decimal_places=2, default=0.0)
	rotation_y = models.DecimalField(_('Display Stands Rotation Y'), max_digits=5, decimal_places=2, default=0.0)
	rotation_z = models.DecimalField(_('Display Stands Rotation Z'), max_digits=5, decimal_places=2, default=0.0)
	scale = models.DecimalField(_('Display Stands Scale'), max_digits=5, decimal_places=2, default=0.0)
	format = models.CharField(_('Display Stands Format'), max_length=20, null=False, blank=False, default='')
	click_event = models.CharField(_('Display Stands Click Event'), max_length=20, null=False, blank=False, default='')
	animation = models.CharField(_('Display Stands Animation'), max_length=20, null=False, blank=False, default='')
	products = models.ManyToManyField(products, verbose_name='Products', related_name='products')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s <%s>' % (self.name, self.type)

	def to_dict(self):
		return {
			'name': self.name,
			'type': self.type,
			'position': {
				'x': self.position_x,
				'y': self.position_y,
				'z': self.position_z,
			},
			'rotation': {
				'x': self.rotation_x,
				'y': self.rotation_y,
				'z': self.rotation_z,
			},
			'scale': self.scale,
			'format': self.format,
			'click_event': self.click_event,
			'animation': self.animation,
			'products': self.products
		}

class campaigns(models.Model):
	class Meta:
		verbose_name = 'Campaigns'
		verbose_name_plural = 'Campaigns'
		# unique_together = ('company', 'title', )

	company = models.CharField(_('Company Name'), max_length=50, null=False, blank=False, default='')
	title = models.CharField(_('Company Title'), max_length=100, null=False, blank=False, default='')
	position_x = models.DecimalField(_('Position X'), max_digits=5, decimal_places=2, default=0.0)
	position_y = models.DecimalField(_('Position Y'), max_digits=5, decimal_places=2, default=0.0)
	position_z = models.DecimalField(_('Position Z'), max_digits=5, decimal_places=2, default=0.0)
	rotation_x = models.DecimalField(_('Rotation X'), max_digits=5, decimal_places=2, default=0.0)
	rotation_y = models.DecimalField(_('Rotation Y'), max_digits=5, decimal_places=2, default=0.0)
	rotation_z = models.DecimalField(_('Rotation Z'), max_digits=5, decimal_places=2, default=0.0)
	display_stands = models.ManyToManyField(display_stands, verbose_name='Display Stands', related_name='display_stands')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s <%s>' % (self.company, self.title)

	def to_dict(self):
		return {
			'company': self.company,
			'title': self.title,
			'position': {
				'x': self.position_x,
				'y': self.position_y,
				'z': self.position_z,
			},
			'rotation': {
				'x': self.rotation_x,
				'y': self.rotation_y,
				'z': self.rotation_z,
			},
			'display_stands': self.display_stands
		}