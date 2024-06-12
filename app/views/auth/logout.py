from django.views.generic import RedirectView
from django.shortcuts import redirect


class logout_view (RedirectView) :
    def get (self, request, **kwargs) : 
        response = redirect('home')
        response.delete_cookie('user')
        return response
        