from django.utils.translation import gettext_lazy as _

CLOUD_TYPE_GCP = 'GCP'
CLOUD_TYPE_AWS = 'AWS'
CLOUD_TYPE_AZURE = 'AZURE'

EVENT_SECONDARY_MEDIA_TYPE_CHOICES = (
    (CLOUD_TYPE_GCP, _("Google Cloud Platform")),
    (CLOUD_TYPE_AWS, _("Amazon Web Services")),
    (CLOUD_TYPE_AZURE, _("Azure")),
)


IDENTITY_DOCUMENT_TYPE_CE = 'ce'
IDENTITY_DOCUMENT_TYPE_DNI = 'dni'
IDENTITY_DOCUMENT_TYPE_PASAPORTE = 'pasaporte'

IDENTITY_DOCUMENT_TYPE_CHOICES = (
    (IDENTITY_DOCUMENT_TYPE_DNI, _("DNI")),
    (IDENTITY_DOCUMENT_TYPE_CE, _("Carnet de extranjería")),
    (IDENTITY_DOCUMENT_TYPE_PASAPORTE, _("Pasaporte"))
)
