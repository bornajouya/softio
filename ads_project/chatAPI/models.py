from django.db import models
from registerAPI.models import User
from datetime import datetime
from adsAPI.models import Ads
# Create your models here.
class chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    time = models.DateTimeField(default=datetime.now())
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    isfirst = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)


# pushed to main