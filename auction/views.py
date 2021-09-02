from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from .forms import Log_form, Player_form
from .models import Login_form,Player,Player_stats,Team,Bids,Logins
# Create your views here.
def login_view(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, "login.html", {'form':fm})

def user_profile(request):
    return render(request, "profile.html", {})

def search_by_category(request):
    return render(request, "searchbycategory.html", {})

def search_by_name(request):
    f_name = request.POST.get('first_name')
    l_name = request.POST.get('last_name')
    print(f_name)
    print(l_name)
    queryset_info = Player.objects.filter(first_name=f_name)
    queryset_new_info = queryset_info.filter(last_name=l_name)
    p_id = queryset_new_info.values('p_id')
    p_info = queryset_new_info.values('p_id', 'speciality', 'age', 'first_name', 'last_name', 'nationality', 'base_price')
    query_stats = Player_stats.objects.filter(p_id__in=p_id)
    req_stats = query_stats.values('matches', 'runs', 'bat_avg', 'strike_rate', 'thirties', 'fifties', 'best_score', 'wickets', 'bowl_avg', 'economy', 'best_bowl_perf')
    l1 = list(p_info)
    l2 = list(req_stats)
    return render(request, "searchbyname.html", {'player_info':l1,'player_stats':l2})

def list_batsman(request):
    queryset_info = Player.objects.filter(speciality="Batsman")
    p_id_list = queryset_info.values('p_id')
    p_info = queryset_info.values('p_id', 'speciality', 'first_name', 'last_name', 'nationality', 'base_price')
    queryset_stats = Player_stats.objects.filter(p_id__in=p_id_list)
    req_stats = queryset_stats.values('matches', 'runs', 'bat_avg', 'strike_rate', 'best_score')
    context={}
    l_main = list(p_id_list)
    l1 = list(p_info)
    l2 = list(req_stats)
    d1 = {}
    d2 = {}
    index = 0
    my_list = []
    list_size = len(l_main)
    for index in range(0,list_size):
        d1 = l1[index]
        d2 = l2[index]
        d1.update(d2)
        my_list.append(d1)
    return render(request, "batsman.html", {'dict':my_list})

def list_bowler(request):
    queryset_info = Player.objects.filter(speciality="Bowler")
    p_id_list = queryset_info.values('p_id')
    p_info = queryset_info.values('p_id', 'speciality', 'first_name', 'last_name', 'nationality', 'base_price')
    queryset_stats = Player_stats.objects.filter(p_id__in=p_id_list)
    req_stats = queryset_stats.values('matches', 'wickets', 'bowl_avg','economy','best_bowl_perf')
    context={}
    l_main = list(p_id_list)
    l1 = list(p_info)
    l2 = list(req_stats)
    d1 = {}
    d2 = {}
    index = 0
    my_list = []
    for index in range(0,len(l_main)):
        d1 = l1[index]
        d2 = l2[index]
        d1.update(d2)
        my_list.append(d1)
    return render(request, "bowler.html", {'dict':my_list})

def list_wicketkeeper(request):
    queryset_info = Player.objects.filter(speciality="WicketKeeper")
    p_id_list = queryset_info.values('p_id')
    p_info = queryset_info.values('p_id', 'speciality', 'first_name', 'last_name', 'nationality', 'base_price')
    queryset_stats = Player_stats.objects.filter(p_id__in=p_id_list)
    req_stats = queryset_stats.values('matches', 'runs', 'bat_avg', 'strike_rate', 'best_score')
    context={}
    l_main = list(p_id_list)
    l1 = list(p_info)
    l2 = list(req_stats)
    d1 = {}
    d2 = {}
    index = 0
    my_list = []
    for index in range(0,len(l_main)):
        d1 = l1[index]
        d2 = l2[index]
        d1.update(d2)
        my_list.append(d1)
    return render(request, "wicketkeeper.html", {'dict':my_list})

def list_allrounder(request):
    queryset_info = Player.objects.filter(speciality="All-rounder")
    p_id_list = queryset_info.values('p_id')
    p_info = queryset_info.values('p_id', 'speciality', 'first_name', 'last_name', 'nationality', 'base_price')
    queryset_stats = Player_stats.objects.filter(p_id__in=p_id_list)
    req_stats = queryset_stats.values('matches','runs','bat_avg','wickets', 'bowl_avg')
    context={}
    l_main = list(p_id_list)
    l1 = list(p_info)
    l2 = list(req_stats)
    d1 = {}
    d2 = {}
    index = 0
    my_list = []
    for index in range(0,len(l_main)):
        d1 = l1[index]
        d2 = l2[index]
        d1.update(d2)
        my_list.append(d1)
    return render(request, "allrounder.html", {'dict':my_list})

def team_info(request):
    t_name = request.POST.get('team_name')
    queryset_info = Team.objects.filter(team_name=t_name)
    req_info = queryset_info.values('team_name', 'homeground', 'Budget', 'owner_fname', 'owner_lname', 'total_players', 'no_of_for', 'no_of_ind')
    l1 = list(req_info)
    print(l1)
    return render(request, "team.html", {'my_list':l1})
    
def bid_player(request):
    p_id_info = request.POST.get('PLAYER_ID')
    u_name = request.POST.get('Uname')
    check = Logins.objects.filter(Username=u_name)
    if (len(check)):
        t=Logins.objects.get(Username=u_name)
    check_next = Bids.objects.filter(p_id=p_id_info)    
    if (len(check_next)):
        value=Bids.objects.get(p_id=p_id_info)
    if (len(check) and len(check_next)):    
        Bids.objects.filter(p_id=p_id_info).update(sold_status=True,bid=bid.value+2500000,team_name=t)
    return render(request, "bid.html", {})

