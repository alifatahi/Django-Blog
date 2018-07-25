from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    # we make auto_now True because its save now over and over not created(add)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # we make it false because its not save now its created
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"id": self.id})
