from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # Pass request and disable validation on normal
    form = PostForm(request.POST or None, request.FILES or None)
    # if valid
    if form.is_valid():
        # save form
        instance = form.save(commit=False)
        # save
        instance.save()
        # Success Message
        messages.success(request, "Successfully Create")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, slug=None):  # Read
    instance = get_object_or_404(Post, slug=slug)
    # encode content for share
    share_string = quote_plus(instance.content)
    context = {
        'instance': instance,
        "title": instance.title,
        'share_string': share_string,
    }
    return render(request, "post_detail.html", context)


def post_list(request):  # List Items
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 5)  # Show 25 contacts per page
    # get Page
    page = request.GET.get('page')
    # Get Value form that Page
    contacts = paginator.get_page(page)

    context = {
        "title": "User",
        'contacts': contacts
    }
    return render(request, "post_list.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    # Pass request and disable validation on normal
    # Pass instance to our form so our form has value from that Id
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    # if valid
    if form.is_valid():
        # save form
        instance = form.save(commit=False)
        # save
        instance.save()
        # Success Message
        messages.success(request, "Successfully Update")
        # Redirect
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'instance': instance,
        "title": instance.title,
        'form': form
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # find
    instance = get_object_or_404(Post, slug=slug)
    # Delete
    instance.delete()
    messages.success(request, "Successfully Delete")
    # Redirect to page
    return redirect('posts:post_list')
