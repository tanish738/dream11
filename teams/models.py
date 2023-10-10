from django.db import models

# Create your models here.
class Player(models.Model):
    POSITION_CHOICES = (
    ('WicketKeeper', 'WicketKeeper'),
    ('Batsman', 'Batsman'),
    ('Bowler', 'Bowler'),
    ('AllRounder', 'AllRounder'),
)
    name = models.CharField(max_length=100 , unique=True)
    points = models.FloatField()
    teams = models.ManyToManyField('Team', auto_created=False ,blank=True)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    no_team = models.IntegerField(default=0) 

    def __str__(self):
        return self.name 


class Team(models.Model):
    name=models.CharField(max_length=100) 
    players = models.ManyToManyField(Player,auto_created=False ,blank=True) 

    def __str__(self):
        return self.name 
