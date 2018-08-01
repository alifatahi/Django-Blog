from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


# upload Location method
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
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


def create_slug(instance, new_slug=None):
    # slugify is for example when our title is new world it becomes new-world for url
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    # Filter slug by id
    qs = Post.objects.filter(slug=slug).order_by("-id")
    # exists is for check true if data received and false if not
    exists = qs.exists()
    if exists:
        # pass our data to string (slug, first id )
        new_slug = "%s-%s" % (slug, qs.first().id)
        # create new slug
        return create_slug(instance, new_slug=new_slug)

    return slug


# Check slug method
def pre_save_post_signal_receiver(sender, instance, *args, **kwargs):
    # if instance dose not have slug then we can create
    if not instance.slug:
        instance.slug = create_slug(instance)


# Connect to pre_save Method to create Slug
pre_save.connect(pre_save_post_signal_receiver, sender=Post)
