from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Video
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
  return render(request, 'base.html')
  
@login_required
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})

@login_required
def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'videos/video_detail.html', {'video': video})
    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('video_list')
    else:
           form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})