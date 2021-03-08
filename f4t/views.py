from django.shortcuts import render
from food4thought.models import Thought, FeedBack, BecomeMember, Testimony
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Q
from .forms import ThoughtForm, FeedBackForm, MemberForm, TestimonyForm


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
    allThoughts = Thought.objects.all().order_by('-date_posted')

    context = {
        'posts': allThoughts
    }

    return render(request, 'f4t/allposts.html', context)


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
                title=title, author=author, bible_quotations=bible_quotations, audio_content=audio_file)
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


def become_member(request):
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
        search_posts = Thought.objects.filter(
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


def testimonies(request):
    all_testimonies = Testimony.objects.all().order_by('-date_of_testimony')

    context = {
        "testimony": all_testimonies
    }

    return render(request, "f4t/testimonies.html", context)


def create_testimony(request):
    success_message = ""
    error_message = ""

    if request.method == "POST":
        form = TestimonyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            testimony = form.cleaned_data.get('testimony')

            Testimony.objects.create(name=name, testimony=testimony)
            return redirect('testimonies')

        else:
            error_message = "sorry something went wrong"
    else:
        form = TestimonyForm()

    context = {
        "form": form,
        "error_message": error_message,
    }

    return render(request, "f4t/testimony_create_form.html", context)


def feedbacks(request):
    all_feeds = FeedBack.objects.all().order_by('-date_of_feedback')

    context = {
        "allfeeds": all_feeds
    }

    return render(request, "f4t/feedbacks.html", context)


def create_feedback(request):
    error_message = ""
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')

            Testimony.objects.create(name=name, message=message)
            return redirect('feedbacks')

        else:
            error_message = "sorry something went wrong"
    else:
        form = FeedBackForm()

    context = {
        "form": form
    }

    return render(request, "f4t/new_feedback.html", context)
