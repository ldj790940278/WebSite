from django.shortcuts import render

# Create your views here.
def myblog(request):
    return render(request,
                  'myblog/myblog.html',
                  )
