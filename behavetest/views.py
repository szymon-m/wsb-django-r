from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def show_user(request):
    return HttpResponse("OK")