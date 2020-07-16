from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from landing.business_logic import get_info_of_account_in_vk


@login_required
def home(request: HttpRequest):
    info_of_account_in_vk = get_info_of_account_in_vk(request)
    return render(request, 'landing/home.html', info_of_account_in_vk)


def login(request: HttpRequest):
    return render(request, 'landing/login.html')
