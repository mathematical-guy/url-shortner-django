from django.db import models
from common_app.models import BaseModel


class ShortenedURL(BaseModel):
    is_disabled = models.BooleanField(default=False)
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    original_url = models.URLField()
    shortened_url = models.URLField()
