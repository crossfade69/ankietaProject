from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from . import forms
from .forms import EditPollForm, EditUsernameForm
from .models import Poll


def teacher_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'registration/login.html', {})


def teacher_logout(request):
    logout(request)
    return redirect('teacher_login')


def teacher_register(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'sukces')
            return redirect('teacher_login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{
        'form':form})

@login_required(login_url='teacher_login')
def edit_profile(request):
    if request.method == 'POST':
        username_form = EditUsernameForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if username_form.is_valid():
            username_form.save()
            messages.success(request, 'Username changed successfully.')
        else:
            messages.error(request, 'Username change failed. Please correct the errors.')

        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Password changed successfully.')
        else:
            messages.error(request, 'Password change failed. Please correct the errors.')

    else:
        username_form = EditUsernameForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'registration/edit_profile.html', {
        'username_form': username_form,
        'password_form': password_form,
    })

#@login_required(login_url='teacher_login')
def panel(request):
    poll = Poll.objects.get(pk=1)
    chart_url = reverse('chart')

    if not request.user.is_authenticated:
        return redirect('login')

    poll_data = {
        'option_a_count': poll.option_a_count,
        'option_b_count': poll.option_b_count,
        'option_c_count': poll.option_c_count,
        'option_d_count': poll.option_d_count,
        'current_access_code': poll.access_code,
        'is_active': poll.is_active,
    }

    if request.method == 'POST':
        form = EditPollForm(request.POST, instance=poll)
        if form.is_valid():
            new_access_code = form.cleaned_data.get('new_access_code')
            if new_access_code and 'change_access_code' in request.POST:
                poll.access_code = new_access_code
                poll.save()
                form.save()

            if 'activate_poll' in request.POST:
                #Session.objects.filter(expire_date__gte=timezone.now()).delete()
                request.session.set_expiry(0)
                poll.is_active = True
                poll.option_a_count = 0
                poll.option_b_count = 0
                poll.option_c_count = 0
                poll.option_d_count = 0
                if new_access_code:
                    poll.access_code = new_access_code
                poll.save()
                form.save()

            if 'deactivate_poll' in request.POST:
                poll.is_active = False
                poll.save()
                form.save()

        else:
            print("Form is invalid: ", form.errors)
    elif 'open_chart' in request.POST:
        return HttpResponseRedirect(chart_url)
    else:
        form = EditPollForm(instance=poll)

    return render(request, 'poll/panel.html',
                  {'poll_data': poll_data, 'form': form,
                   'chart_url': chart_url, 'current_access_code': poll.access_code})

def chart(request):
    current_access_code = request.GET.get('current_access_code', 'default_access_code')
    poll_status = request.GET.get('poll_status', False)

    poll = Poll.objects.get_or_create(pk=1, defaults={'access_code': current_access_code})[0]
    chart_data = {
        'Option A': poll.option_a_count,
        'Option B': poll.option_b_count,
        'Option C': poll.option_c_count,
        'Option D': poll.option_d_count,
    }

    return render(request, 'poll/chart.html',
                  {'data': chart_data, 'current_access_code': current_access_code, 'poll_status': poll_status})

def access(request):
    poll = Poll.objects.get(pk=1)

    if request.session.get('has_entered_code'):
        return redirect('vote')

    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        try:
            poll = get_object_or_404(Poll, access_code=access_code)

            if not poll.is_active:
                return render(request, 'poll/notready.html')

            request.session['has_entered_code'] = True
            return redirect('vote')

        except Http404:
            messages.error(request, 'Invalid access code. Please try again.')

    if not poll.is_active:
        return render(request, 'poll/notready.html')

    return render(request, 'poll/password.html')


def vote(request):
    poll = Poll.objects.get()

    if not request.session.get('has_entered_code'):
        return redirect('access')

    if not poll.is_active:
        return render(request, 'poll/notready.html')

    if 'has_voted' in request.session:
        return render(request, 'poll/thankyou.html')


    if request.method == 'POST':
        selected_option = request.POST.get('poll')
        if selected_option in {'option_a', 'option_b', 'option_c', 'option_d'}:
            setattr(poll, f'{selected_option}_count', getattr(poll, f'{selected_option}_count') + 1)
            poll.save()

            request.session['has_voted'] = True

            return render(request, 'poll/thankyou.html')
        else:
            return HttpResponse('Invalid form option')

    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)


