from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#A09 security logging and monitoring failures failed login attempts are not logged as security events

#A09 fix: log failed login attempts as security events
#from django.contrib.auth.signals import user_login_failed
#from django.dispatch import receiver
#import logging

#security_logger = logging.getLogger("django.security")

#@receiver(user_login_failed)
#def log_failed_login(sender, credentials, request, **kwargs):
   #security_logger.warning("Failed login attempt")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        form = DiaryEntryForm()

    search = request.GET.get('search')
    if search:
        #A03 injection: user input is used directly into SQL
        query = f"SELECT * FROM diary_diaryentry WHERE title LIKE '%%{search}%%'"
        entries = DiaryEntry.objects.raw(query)
        #A03 fix: use SQL parameters to prevent SQL injection
       #query = "SELECT * FROM diary_diaryentry WHERE user_id = %s AND title LIKE %s"
      #entries = DiaryEntry.objects.raw(query, [request.user.id, f"%{search}%"])
    else:

        entries = DiaryEntry.objects.filter(
            user=request.user
        ).order_by('-created_at')

    return render(request, 'diary/home.html', {
        'form': form,
        'entries': entries
    })


@login_required
def entry_detail(request, entry_id):
    #A01: Broken Access Control: entry is retrieved without checking its owner
    entry = get_object_or_404(
       DiaryEntry,
        id=entry_id,
   )

#Fix: Check if the entry belongs to the user that is logged in
     #entry = get_object_or_404(
        #DiaryEntry,
        #id=entry_id,
        #user=request.user
    #)
    return render(request, 'diary/entry_detail.html', {
    'entry': entry
    })
