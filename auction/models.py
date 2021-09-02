from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class Login_form(models.Model):
    Username = models.CharField(max_length=6, primary_key=True)
    Password = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.Username

class Team(models.Model):
    team_name = models.CharField(max_length=50, primary_key=True)
    homeground = models.CharField(max_length=20, null=False)
    Budget = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(600000000)])
    owner_fname = models.CharField(max_length=20, null=False)
    owner_mname = models.CharField(max_length=20, null=True)
    owner_lname = models.CharField(max_length=20, null=False)
    total_players = models.IntegerField(validators=[MaxValueValidator(25)])
    no_of_for = models.IntegerField()
    no_of_ind = models.IntegerField()

class Logins(models.Model):
    team_name=models.ForeignKey(Team, on_delete=models.CASCADE)
    Username=models.ForeignKey(Login_form, on_delete=models.CASCADE)

class Player(models.Model):
    p_id = models.CharField(max_length=4,primary_key=True)
    speciality = models.CharField(max_length=15)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    nationality = models.CharField(max_length=20)
    base_price = models.IntegerField(validators=[MinValueValidator(10000000),MaxValueValidator(20000000)])

class Player_stats(models.Model):
    p_id = models.ForeignKey(Player,on_delete=models.CASCADE)
    matches = models.IntegerField()
    bat_avg = models.DecimalField(max_digits=4,decimal_places=2, null=True)
    strike_rate = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    runs = models.IntegerField()
    thirties = models.IntegerField()
    fifties = models.IntegerField()
    best_score = models.IntegerField()
    wickets = models.IntegerField()
    bowl_avg = models.DecimalField(max_digits=4,decimal_places=2, null=True)
    economy = models.DecimalField(max_digits=4,decimal_places=2, null=True)
    best_bowl_perf = models.CharField(max_length=6, null=True)

class Bids(models.Model):
    bid=models.IntegerField()
    sold_status=models.BooleanField(default=False)
    p_id=models.ForeignKey(Player,on_delete=models.CASCADE)
    team_name=models.ForeignKey(Team,on_delete=models.CASCADE)
    



