from django.db import models

class Blogs(models.Model):
	title = models.CharField(max_length=225)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='image')