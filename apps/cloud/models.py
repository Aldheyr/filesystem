from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel


class Provider(BaseModel):

    name = models.CharField(
        verbose_name=_('Cloud'),
        max_length=128,
        unique=True
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=128,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Nube")
        verbose_name_plural = _("Nubes")


class TypeService(BaseModel):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=128,
        unique=True
    )

    nombre = models.CharField(
        verbose_name=_('Nombre'),
        max_length=128,
        unique=True,
        blank=True,
        null=True
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=128,
        unique=True
    )

    cloud = models.ForeignKey(
        Provider,
        verbose_name=_('Nube'),
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tipo de servicio")
        verbose_name_plural = _("Tipos de servicio")


class Service(BaseModel):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=128,
        unique=True
    )

    nombre = models.CharField(
        verbose_name=_('Nombre'),
        max_length=128,
        unique=True,
        blank=True,
        null=True
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=128,
        unique=True
    )

    image = models.ImageField(
        verbose_name=_('Logo'),
        upload_to='Services/',
        blank=True,
        null=True
    )

    type_service = models.ForeignKey(
        TypeService,
        verbose_name=_('Tipo de servicio'),
        on_delete=models.PROTECT
    )

    @property
    def slug_cloud(self):
        return self.type_service.cloud.slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Servicio")
        verbose_name_plural = _("Servicios")


class Region(BaseModel):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=128,
        unique=True
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=128,
        unique=True
    )

    provider = models.ForeignKey(
        Provider,
        verbose_name=_('Proveedor'),
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regiones")


class Environment(BaseModel):

    name = models.CharField(
        verbose_name=_('Nombre'),
        max_length=128,
        unique=True
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=128,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Ambiente")
        verbose_name_plural = _("Ambientes")
