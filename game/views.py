from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def connect(request):
    return render(request, 'game/connect.html')


@login_required
def dashboard(request):
    return render(request, 'game/dashboard.html')