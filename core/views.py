import imp
from django.shortcuts import redirect, render
from . models import Work, Follow
from accounts.models import Profile
from .forms import Workform, Commentform

def home(request):
    works = Work.objects.all()
    context = {'works':works}
    return render(request, 'index.html', context)

def singlework(request, pk):
    work = Work.objects.get(id = pk)
    profile = request.user.profile
    form =Commentform()

    if request.method == 'POST':
        form = Commentform(request.POST)
        comment = form.save(commit=False)
        comment.work = work
        comment.profile = request.user.profile
        comment.save()
        return redirect('singlework', pk=work.id)


    follow = Follow.objects.filter(following=profile, follower=work.profile.id)
    if follow:
        followed = True
    else:
        followed = False


    context = {'work':work, 'form': form, 'profile': profile, 'followed': followed}
    return render(request, 'singlework.html', context)
    
    
def creatework(request):
    profile = request.user.profile
    form = Workform()
    if request.method == 'POST':
        form = Workform(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit = False)
            work.profile = profile
            work.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'creatework.html', context)



def follow(request, pk):
    profile = request.user.profile
    follower = Profile.objects.get(id = pk)
    follow = Follow.objects.create(following = profile, follower= follower)
    return redirect(request.META.get('HTTP_REFERER'))
    



def unfollow(request, pk):
    profile = request.user.profile
    follower = Profile.objects.get(id=pk)
    follow = Follow.objects.filter(following=profile, follower=follower)
    follow.delete()
    return redirect(request.META.get('HTTP_REFERER'))