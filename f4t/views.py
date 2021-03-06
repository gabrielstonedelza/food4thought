from django.shortcuts import render
from food4thought.models import Thought, Comment, BecomeMember
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Q
from .forms import ThoughtForm, CommentsForm, MemberForm


def csrf_failure(request, reason=""):
    return render(request, "f4t/403_csrf.html")


def post_home(request):
    posts = Thought.objects.all().order_by('-date_posted')
    post_today = Thought.objects.all().order_by('-date_posted')[:1]

    context = {
        'posts': posts,
        'post_today': post_today
    }

    return render(request, 'f4t/post_home.html', context)


def all_posts(request):
    all_posts = Thought.objects.all().order_by('-date_posted')

    context = {
        'posts': all_posts
    }

    return render(request, 'f4t/allposts.html', context)


def thought_detail(request, id):
    post = get_object_or_404(Thought, id=id)

    comments = Comment.objects.filter(post=post).order_by('-date_of_comment')
    comments_count = comments.count()

    form = CommentsForm()
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            comment = request.POST.get('comment')
            comment = Comment.objects.create(name=name,comment=comment)
            comment.save()

        else:
            form = CommentsForm()

    if post:
        post.views += 1
        post.save()

    context = {
        "form": form,
        "post": post,
        "comments": comments,
        "comments_count": comments_count,
    }

    if request.is_ajax():
        comment = render_to_string("f4t/comment_form.html", context, request=request)
        return JsonResponse({"comments": comment})

    return render(request, "f4t/post_detail.html", context)


def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    post.likes += 1
    post.save()

    context = {
        "post": post,
    }

    if request.is_ajax():
        likeblog = render_to_string("f4t/like_section.html", context, request=request)
        return JsonResponse({"like": likeblog})


def create_post(request):
    success_message = ""
    error_message = ""

    if request.method == "POST":
        form = ThoughtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            bible_quotations = form.cleaned_data.get('bible_quotations')
            audio_file = form.cleaned_data.get('audio_content')
            Thought.objects.create(
                title=title, author=author,  bible_quotations=bible_quotations, audio_content=audio_file)
            return redirect('post_home')

        else:
            error_message = "sorry something went wrong"
    else:
        form = ThoughtForm()

    context = {
        "form": form,
        "error_message": error_message,
    }

    return render(request, "f4t/post_create_form.html", context)


def members(request):
    all_members = BecomeMember.objects.all().order_by('-date_joined')

    context = {
        'all_members': all_members
    }

    return render(request, 'f4t/members.html', context)


def become_amember(request):
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            
            BecomeMember.objects.create(name=name, email=email, phone=phone)
            return redirect('members')

    else:
        form = MemberForm()

    context = {
        "form": form
    }

    return render(request, 'f4t/become_member.html', context)


def about(request):
    return render(request, 'f4t/about_f4t.html')


def search_queries(request):
    global search_posts, rooms
    query = request.GET.get('q', None)
    if query is not None:
        search_posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query)
        )

    context = {
        'posts': search_posts,
    }
    if request.is_ajax():
        html = render_to_string("f4t/search_list.html", context, request=request)
        return JsonResponse({
            'form': html
        })
