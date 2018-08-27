from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


# Create your views here.
def logout_view(request):
    """logout users"""
    logout(request)
    return HttpResponseRedirect(reverse('stuapp:index'))


def register(request):
    """register users"""
    if settings.REG:
        if request.method != 'POST':
            # no data post, create a empty form.
            form = UserCreationForm()
        else:
            # handle with posted data.
            form = UserCreationForm(data=request.POST)

            if form.is_valid():
                new_user = form.save()
                # let user auto login and redirect to index page.
                authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('stuapp:index'))
        context = {'form': form}
        return render(request, 'users/register.html', context)
    else:
        return HttpResponse("Register Not Allowed Now!!!")
