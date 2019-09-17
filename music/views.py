from django.shortcuts import render

# Create your views here.
def music(request):
    return render(request,
                  'music/music.html',
                  )
def album(request):
    return render(request,
                  'music/album.html',
                  )
