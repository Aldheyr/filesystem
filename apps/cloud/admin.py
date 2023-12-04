from django.contrib import admin
from .models import (
    Provider,
    TypeService,
    Service,
    Region,
    Environment,
)

admin.site.register(Provider)
admin.site.register(TypeService)
admin.site.register(Service)
admin.site.register(Region)
admin.site.register(Environment)
