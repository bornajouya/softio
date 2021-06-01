from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.html import mark_safe
from registerAPI.models import User

class Ads(models.Model):
    title = models.CharField(default="no title", max_length=200)
    description = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="images", blank=True, null=True)
    publish_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="80" height="80" />' % self.photo)

