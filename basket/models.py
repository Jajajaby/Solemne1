from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES

class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name


class Player(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	nickname = models.CharField(max_length=50)
	birthday = models.DateField() 
	age = models.IntegerField()
	rut = models.CharField(max_length=8)
	email = models.EmailField()
	height = models.DecimalField(max_digits=4, decimal_places=2, default=0) #estatura 
	weight = models.DecimalField(max_digits=4, decimal_places=2, default=0) #peso 
	picture = models.ImageField(upload_to='media')
	position = models.CharField(max_length=15, choices=POSITION_PLAYER_CHOICES)
	dv = models.PositiveIntegerField()

	def full_rut(self):
		return '{}-{}' . format(self.rut, self.dv)

	def __str__(self):
		return self.name


class Coach(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	email = models.EmailField()
	rut = models.CharField(max_length=15)
	nickname = models.CharField(max_length=50)
	dv = models.PositiveIntegerField()

	def __str__(self):
		return self.name

#     question = models.ForeignKey(Question, on_delete=models.CASCADE)