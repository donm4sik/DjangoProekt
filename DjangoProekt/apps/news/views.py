from django.shortcuts import render

def greeting(request):
    return render(
        request=request,
        template_name='news/greeting.html'
    )

