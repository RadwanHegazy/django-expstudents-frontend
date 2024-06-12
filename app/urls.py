from django.urls import path
from .views.auth import login, register, logout
from .views import home, upload_post

urlpatterns = [
    path('', home.home_view.as_view(), name='home'),
    path('post/upload/', upload_post.post_view.as_view(), name='post'),
    path('user/login/',login.login_view.as_view(),name='login'),
    path('user/register/',register.register_view.as_view(),name='register'),
    path('user/logout/',logout.logout_view.as_view(),name='logout'),
]