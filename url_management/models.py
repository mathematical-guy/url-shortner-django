from django.db import models
from common_app.models import BaseModel
from url_management.utils import shortend_url_object_id_generator


class ShortenedURL(BaseModel):
    id = models.CharField(
        max_length=24, default=shortend_url_object_id_generator,
        primary_key=True, unique=True
    )
    is_disabled = models.BooleanField(default=False)
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    original_url = models.URLField()
