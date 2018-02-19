from django.db import models

platform_choices = (
	('PC', 'PC'),
	('PlayStation', 'PlayStation'),
	('XBOX', 'XBOX')

	)

class Game(models.Model):
	name = models.CharField(max_length=225)
	release_date =  models.DateField(null=True, blank=True)
	multiplayer = models.BooleanField(default=True)
	image = models.ImageField(null=True, blank=True, upload_to="post_images")
	platforms = models.CharField(max_length= 100, choices=platform_choices)

	def __str__(self):
		return self.name

