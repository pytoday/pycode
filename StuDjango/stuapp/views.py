from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# from django.shortcuts import HttpResponse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """django index page"""
    # return HttpResponse("Hello World for index.")
    return render(request, 'stuapp/index.html')


def topics(request):
    """all topics page"""
    topics = Topic.objects.order_by('date_added')
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'stuapp/topics.html', context)


def topic(request, topic_id):
    """show topic and entries"""
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return render(request, 'stuapp/404.html')
    # if topic.owner != request.user:
    #     raise Http404
    else:
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries, 'topic_id': topic_id}
        return render(request, 'stuapp/topic.html', context)


def nothing(request):
    """nothing here"""
    return render(request, 'stuapp/404.html')


@login_required
def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        # no commit data? create a new form
        form = TopicForm()
    else:
        # POST committed data, handle with data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # form.save()
            return HttpResponseRedirect(reverse('stuapp:topics'))

    context = {'form': form}
    return render(request, 'stuapp/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """add entries for topic"""
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return render(request, 'stuapp/404.html')
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # no commit data? create a entry form
        form = EntryForm()
    else:
        # POST committed data
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('stuapp:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'stuapp/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """edit entry"""
    try:
        entry = Entry.objects.get(id=entry_id)
    except Entry.DoesNotExist:
        return render(request, 'stuapp/404.html')
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('stuapp:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'stuapp/edit_entry.html', context)
