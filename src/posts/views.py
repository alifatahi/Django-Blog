from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<p>Hello</p>")


def post_detail(request):  # Read
    return HttpResponse("<p>Hello</p>")


def post_list(request):  # List Items
    queryset = Post.objects.all()
    # if request.user.is_authenticated:
    #     context = {
    #         "title": "Admin"
    #     }
    # else:
    #     context = {
    #         "title": "User"
    #     }
    context = {
        'object_list' : queryset,
        "title": "User"
    }
    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<p>Hello</p>")


def post_delete(request):
    return HttpResponse("<p>Hello</p>")
