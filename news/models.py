from django.db import models


class News(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
