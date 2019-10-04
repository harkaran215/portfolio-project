from django.db import models

class Blogs(models.Model):
	title = models.CharField(max_length=225)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='image')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def date_only(self):
		return self.pub_date.strftime('%b %e %Y')