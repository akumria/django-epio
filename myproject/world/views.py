from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page.

    Typically this will have a login screen on it.
    """
    return render(request, "www/home.html")
