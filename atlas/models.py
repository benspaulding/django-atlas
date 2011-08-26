"""
Models for an atlas application.

"""

import datetime

from django.conf import settings
from django.db import models
from template_utils.markup import formatter


class Country(models.Model):
    """
    A country on planet earth, plain and simple.

    """

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, help_text=u'Used in the URL for the \
        country. Must be unique.')

    class Meta:
        verbose_name_plural = u'countries'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class State(models.Model):
    """
    A state, province, etc. in a country.

    """

    name = models.CharField(max_length=250)
    slug = models.SlugField(help_text=u'Used in the URL for the state. Must \
        be unique within its country.')
    country = models.ForeignKey(Country, related_name='states')

    class Meta:
        ordering = ['country', 'name']

    def __unicode__(self):
        return self.name


class City(models.Model):
    """
    A city, town, hamlet etc. in a state, or province, etc. and county,
    borough, etc.

    """

    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text=u'Used in the URL for the \
        city. Must be unique within its state.')
    state = models.ForeignKey(State, related_name='cities')
    county = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = u'cities'
        ordering = ['state', 'county', 'name']

    def __unicode__(self):
        return self.name


class LocationType(models.Model):
    """
    A type of location, i.e. home, hotel, restaurant, etc.

    """

    kind = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, help_text=u'Used in the URL for the \
        location type. Must be unique.')

    class Meta:
        ordering = ['kind']

    def __unicode__(self):
        return self.kind


class Location(models.Model):
    """
    A specific location within a city, town, hamlet etc.

    """

    name = models.CharField(max_length=250)
    address_1 = models.CharField(max_length=250, blank=True)
    address_2 = models.CharField(max_length=250, blank=True)
    city = models.ForeignKey(City, related_name='locations')
    state = models.ForeignKey(State, related_name='locations')
    country = models.ForeignKey(Country, related_name='locations')
    zip = models.CharField(u'ZIP / Postal code', max_length=36, blank=True)

    location_type = models.ForeignKey(LocationType, related_name='locations')
    neighborhood = models.CharField(max_length=250, blank=True)
    description_txt = models.TextField(u'Description', blank=True,
        help_text=u'A short description of the location.<br />\
        <a href="http://daringfireball.net/projects/markdown/dingus">\
        Markdown</a> syntax allowed.')
    description_xml = models.TextField(editable=False, blank=True)

    latitude = models.FloatField(blank=True, null=True, help_text=u'<a \
        href="http://getlatlon.net/" title="Brillant tool by Simon Willison">\
        GetLatLon.net</a> will help.')
    longitude = models.FloatField(blank=True, null=True, help_text=u'<a \
        href="http://getlatlon.net/" title="Brillant tool by Simon Willison">\
        GetLatLon.net</a> will help.')

    class Meta:
        ordering = ['country', 'state', 'name']

    def __unicode__(self):
        return self.name

    def save(self):
        self.description_xml = formatter(self.description_txt)
        super(Location, self).save()
