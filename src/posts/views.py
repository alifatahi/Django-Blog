from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_create(request):
    # Pass request and disable validation on normal
    form = PostForm(request.POST or None)
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


def post_detail(request, id=None):  # Read
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        "title": instance.title
    }
    return render(request, "post_detail.html", context)


def post_list(request):  # List Items
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
        "title": "User",
        'contacts': contacts
    }
    return render(request, "post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    # Pass request and disable validation on normal
    # Pass instance to our form so our form has value from that Id
    form = PostForm(request.POST or None, instance=instance)
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


def post_delete(request, id=None):
    # find
    instance = get_object_or_404(Post, id=id)
    # Delete
    instance.delete()
    messages.success(request, "Successfully Delete")
    # Redirect to page
    return redirect('posts:post_list')
