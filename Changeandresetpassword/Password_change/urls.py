from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import logout_view, login_view, register_view, \
    home_view, change_pass_view,show_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('changepassword/', change_pass_view, name='changepassword'),
    path('show/',show_view,name='show'),

]

