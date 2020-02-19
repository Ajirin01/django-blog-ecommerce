from django.db import models

# Create your models here.


class posts(models.Model):
    post_title = models.CharField(max_length=30)
    post_body = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'posts'
    def __str__(self):
        return self.post_title