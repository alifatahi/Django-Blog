from django.contrib import admin

# Register your models here.
# Since we are in same Directory we pass .models instead of posts.models
from .models import Post

admin.site.register(Post)

