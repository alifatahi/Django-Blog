from django.contrib import admin

# Register your models here.
# Since we are in same Directory we pass .models instead of posts.models
from .models import Post


# Class which inheritance from ModelAdmin
class PostModelAdmin(admin.ModelAdmin):
    # Show 2 thing in our admin (Title,Time)
    list_display = ["title", "updated", "timestamp"]
    # Declare Which Item to Link
    list_display_links = ["timestamp"]
    # Add Filtering Like See Last Post in 7 Day
    list_filter = ["updated", "timestamp"]
    # Make Our Field Editable in Main Admin Page(It Should Be in List Display)
    list_editable = ["title"]
    # Make Search and Declare Field to Search In
    search_fields = ["title", "content"]

    # Declare Model
    class Meta:
        model = Post


# Register our Customize Class For Post Admin
admin.site.register(Post, PostModelAdmin)
