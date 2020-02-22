from django.http import HttpResponse
def user(request):
    return HttpResponse('<h1>you are successfully signed in </h1>')