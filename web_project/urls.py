"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from auction import views
urlpatterns = [
    path('', views.login_view),
    path('profile/', views.user_profile, name='profile'),
    path('searchbycategory/', views.search_by_category, name='searchbycategory'),
    path('searchbyname/', views.search_by_name, name='searchbyname'),
    path('admin/', admin.site.urls),
    path('batsman/', views.list_batsman, name="listbatsman"),
    path('bowler/', views.list_bowler, name="listbowler"),
    path('wicketkeeper/', views.list_wicketkeeper, name="listwicketkeeper"),
    path('bowler/', views.list_allrounder, name="listallrounder"),
    path('team/', views.team_info, name="teaminfo"),
    path('bid/', views.bid_player, name="bidplayer"),
    path('allrounder/',views.list_allrounder,name='listallrounder')
]
