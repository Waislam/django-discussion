from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


# Create your models here.
class Board(models.Model):
	name =models.CharField(max_length=30, unique=True)
	description =models.CharField(max_length=100)

	def __str__ (self):
		return self.name

	def get_post_count(self):
		return Post.objects.filter(topic__board=self).count()

	def get_last_post(self):
		return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
	subject=models.CharField(max_length=200)
	starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='topics')
	board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
	last_updated = models.DateTimeField(auto_now_add=True)
	views =models.PositiveIntegerField(default=0)
	def __str__ (self):
		return self.subject

class Post (models.Model):
	message =models.TextField(max_length=4000)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
	topic =models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')

	def __str__ (self):
		truncated_message=Truncator(self.message)
		return truncated_message.chars(30)
				