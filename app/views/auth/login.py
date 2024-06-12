from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class login_view (TemplateView) :
    template_name = 'login.html'

    def post(self, request, **kwargs) :
        def get_(key): return request.POST.get(key, None)

        data = {
            'phonenumber' : get_('phonenumber'),
            'password' : get_('password'),
        }
        
        action = Action(
            url=MAIN_URL + '/user/auth/login/',
            data=data
        )

        action.post()

        if action.is_valid():
            response = redirect('home')
            response.set_cookie('user', action.json_data['token'])
            return response
        
        messages.error(request, 'invalid phonenumber or password')
        return redirect('login')
        