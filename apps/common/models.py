import uuid
from django.db import models
from django.conf import settings
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from .middleware import CurrentUserMiddleware


class BaseManager(models.Manager):

    def default(self):
        return self.all()


class BaseQuerySet(models.QuerySet):
    pass


class BaseModel(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(
        verbose_name=_('Esta activo?'),
        default=True
    )

    created_at = models.DateTimeField(
        verbose_name=_('Fecha y hora de creación'),
        auto_now_add=True,
        null=True,
        blank=True
    )

    updated_at = models.DateTimeField(
        verbose_name=_('Fecha y hora de actualización'),
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name=_("Creado por"),
                                   related_name="%(app_label)s_%(class)s_created",
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True,
                                   )

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name=_("Actualizado por"),
                                   related_name="%(app_label)s_%(class)s_updated",
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True,
                                   )

    class Meta:
        abstract = True

    @staticmethod
    def get_current_user():
        return CurrentUserMiddleware.get_current_user()

    def set_user_fields(self, user):
        if user and user.pk:
            if not self.pk and not self.created_by:
                self.created_by = user
            if self.is_being_updated():
                if not self.updated_by:
                    self.updated_by = user

    def is_being_updated(self):
        return self.created_at and localtime() > self.created_at

    def save(self, *args, **kwargs):
        current_user = self.get_current_user()
        if current_user is not None:
            self.set_user_fields(current_user)
        if self.is_being_updated():
            self.updated_at = localtime()
        super(BaseModel, self).save(*args, **kwargs)

    def get_content_type(self):
        return ContentType.objects.get_for_model(self)
