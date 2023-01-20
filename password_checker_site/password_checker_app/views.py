from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from zxcvbn import zxcvbn

from password_checker_app.forms import PasswordCheckerForm

# Create your views here.
class PasswordCheckerView(View):
    def get(self, request):
        
        password_form = PasswordCheckerForm()
        
        context = {
            'form': password_form,
            'offline_fast_hash':'',
            'offline_slow_hash':'',
            'online_no_throttling':'',
            'online_throttling':'',
        }
        
        return render(
            request=request,
            template_name='index.html',
            context=context,
        )
    
    def post(self, request):
        
        result = zxcvbn(request.POST['pw_input'])
        
        print(result)
        
        password_form = PasswordCheckerForm()
        
        context = {
            'form': password_form,
            'offline_fast_hash': result['crack_times_display']['offline_fast_hashing_1e10_per_second'],
            'offline_slow_hash': result['crack_times_display']['offline_slow_hashing_1e4_per_second'],
            'online_no_throttling':result['crack_times_display']['online_no_throttling_10_per_second'],
            'online_throttling':result['crack_times_display']['online_throttling_100_per_hour'],
        }
        
        return render(
            request=request,
            template_name='index.html',
            context=context,
        )
        