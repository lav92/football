from django.db import models

# Create your models here.


class Team(models.Model):
    fullname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, unique=True)
    tla = models.CharField(max_length=50, blank=True)
    logo = models.CharField(max_length=255, blank=True)
    data_football_id = models.IntegerField()

    def __str__(self):
        return self.name


class Table(models.Model):
    position = models.IntegerField()
    team = models.OneToOneField(Team, on_delete=models.SET_NULL, null=True)
    played_games = models.IntegerField()
    won = models.IntegerField()
    draw = models.IntegerField()
    lost = models.IntegerField()
    points = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    goal_difference = models.IntegerField()

    class Meta:
        ordering = ['position']


class Player(models.Model):
    name = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=100, blank=True)
    data_football_id = models.IntegerField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='players', null=True)

    def __str__(self):
        return self.name


class TableScorers(models.Model):
    players = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True)
    goals = models.IntegerField(blank=True)
    assists = models.IntegerField(blank=True)

    class Meta:
        ordering = ['-goals']
