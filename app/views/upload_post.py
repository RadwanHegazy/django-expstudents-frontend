from django.views import View
from globals.request_manager import Action
from globals.decorators import login_required
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from django.contrib import messages

class post_view (View) :

    @login_required
    def get(self, request, **kwargs) : 
        return render(request,'post.html')
    
    @login_required
    def post(self, request, **kwargs) : 
        headers = kwargs['headers']
        action = Action(
            url = MAIN_URL + '/post/create/',
            headers=headers,
            data={
                **request.POST
            }   
        )
        action.post()
        if action.is_valid():
            return redirect('home')
        
        messages.error(request, 'an error accoured ')
        return redirect('post')

