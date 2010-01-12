from django.db import models
from django.utils.translation import ugettext_lazy as _


class AtlasUniqueBase(models.Model):
    """
    Base class for atlas models whose name & slug fields are unique throughout
    the table.

    """

    name = models.CharField(_(u'name'), max_length=255, unique=True)
    slug = models.SlugField(_(u'slug'), unique=True)

    class Meta:
        abstract = True
        ordering = ('name', )

    def __unicode__(self):
        return self.name


class AtlasBase(models.Model):
    """
    Base class for atlas models whose name & slug fields are not unique
    throughout the table.

    """

    name = models.CharField(_(u'name'), max_length=255)
    slug = models.SlugField(_(u'slug'))

    class Meta:
        abstract = True
        ordering = ('name', )

    def __unicode__(self):
        return self.name


class Country(AtlasUniqueBase):
    """A country on planet earth, plain and simple."""

    class Meta(AtlasUniqueBase.Meta):
        verbose_name = _(u'country')
        verbose_name_plural = _(u'countries')


class State(AtlasBase):
    """A state, province, etc. in a country."""

    country = models.ForeignKey(Country, verbose_name=_(u'country'),
        related_name='states')

    class Meta(AtlasBase.Meta):
        ordering = ('country', 'name')
        unique_together = (('name', 'country'), ('slug', 'country'))
        verbose_name = _(u'state')
        verbose_name_plural = _(u'states')


class City(AtlasBase):
    """
    A city, town, hamlet etc. in a state, or province, etc. and county,
    borough, etc.

    """

    state = models.ForeignKey(State, related_name='cities',
        help_text=_(u'Or province, etc.'))
    county = models.CharField(max_length=255, blank=True,
        help_text=_(u'Or burough, or whatever.'))

    class Meta(AtlasBase.Meta):
        ordering = ('state', 'name')
        unique_together = (('name', 'state'), ('slug', 'state'))
        verbose_name = _(u'city')
        verbose_name_plural = _(u'cities')


class LocationType(AtlasUniqueBase):
    """A type of location, e.g. home, hotel, restaurant, etc."""

    class Meta(AtlasUniqueBase.Meta):
        verbose_name = _(u'location type')
        verbose_name_plural = _(u'location types')


class Location(AtlasBase):
    """A specific location within a city, town, hamlet etc."""

    address_1 = models.CharField(_(u'adreess1'), max_length=255, blank=True)
    address_2 = models.CharField(_(u'address 2'), max_length=255, blank=True)
    city = models.ForeignKey(City, verbose_name=_(u'city'),
        related_name='locations')
    zip = models.CharField(_(u'ZIP code'), max_length=36, blank=True,
        help_text=_(u'Or postal code; whatever you got.'))

    neighborhood = models.CharField(_(u'neighborhood'), max_length=255,
        blank=True)
    location_type = models.ForeignKey(LocationType,
        verbose_name=_(u'location type'), related_name='locations')
    description = models.TextField(_(u'description'), blank=True)

    latitude = models.FloatField(_('latitude'), blank=True, null=True)
    longitude = models.FloatField(_('longitude'), blank=True, null=True)

    class Meta(AtlasBase.Meta):
        ordering = ('city__state__country', 'city__state', 'city', 'name')
        unique_together = (('slug', 'city'), )
        verbose_name = _(u'location')
        verbose_name_plural = _(u'locations')
