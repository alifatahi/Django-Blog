from django.db import models
from django.urls import reverse

# upload Location method
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    # Image Field(Location,nullable,blank,height format,width format)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    # we make auto_now True because its save now over and over not created(add)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # we make it false because its not save now its created
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]
