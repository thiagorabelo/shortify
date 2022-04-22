from hashlib import md5

from django.db import models, IntegrityError
from django.contrib.auth.models import User

# Create your models here.


# https://www.digitalocean.com/community/tutorials/how-to-create-a-url-shortener-with-django-and-graphql-pt
class ShortURI(models.Model):
    MAX_ALLOWED_COLLISIONS = 3

    full_uri = models.URLField("Full URI", help_text="The actual URI", blank=False, max_length=255)
    uri_hash = models.CharField("Hash Code", unique=True, max_length=10, blank=False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    description = models.CharField("Description", help_text="Helps you remember what this URI is about", max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = "Short URI"
        verbose_name_plural = "Shorts URI"
    
    def __str__(self):
        return f"ShortURI(full_uri='{self.full_uri}')"
    
    def __repr__(self):
        return str(self)

    def save(self, *args, **kwargs):
        for try_ in range(self.MAX_ALLOWED_COLLISIONS):
            try:
                if not self.pk:
                    self._create_hash(try_)
                return super().save(*args, **kwargs)
            except IntegrityError as ex:
                if (try_ + 1) >= self.MAX_ALLOWED_COLLISIONS:
                    raise IntegrityError(f"Max try save achieved ({try_})") from ex
    
    def _create_hash(self, try_=0):
        from django.conf import settings
        msg = settings.SECRET_KEY + self.full_uri + self.user.username + str(try_)
        self.uri_hash = md5(msg.encode()).hexdigest()[:10]
