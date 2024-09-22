from django.db import models

class AppClient(models.Model):
    postId = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    body = models.CharField(max_length=60)
    def __str__(self):
        return self.postId