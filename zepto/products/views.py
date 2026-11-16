from django.http import HttpResponse

def product_list(request):
    return HttpResponse("Welcome to Zepto Products Page!")