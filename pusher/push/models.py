from django.db import models


class PostRow(models.Model):
    external_id = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    added_in_social_media = models.CharField(max_length=256)
    # group_name = models.CharField(max_length=256)
    group_id = models.CharField(max_length=256)
    post_value = models.CharField(max_length=256)


