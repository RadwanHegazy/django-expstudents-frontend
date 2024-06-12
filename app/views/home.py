from django.views import View
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.shortcuts import render

class home_view (View) :
    template_name = 'index.html'

    def get(self, request, **kwargs) :
        action = Action(
            url = MAIN_URL + '/post/get/',
        )
        action.get()
        data = action.json_data
        return render(request, 'index.html', {'posts':data})