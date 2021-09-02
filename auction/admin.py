from django.contrib import admin
from .models import Login_form,Team,Logins,Player,Player_stats,Bids 
# Register your models here.
admin.site.register(Login_form)
admin.site.register(Team)
admin.site.register(Logins)
admin.site.register(Player)
admin.site.register(Player_stats)
admin.site.register(Bids)


