from django.http import HttpResponse

def NotFound(request, arg):
    return HttpResponse("Page Not Found!!")
