from django import forms
from .models import Topic
from .models import Post


class PostForm(forms.ModelForm):
	message =forms.CharField(widget=forms.Textarea(attrs={'placeholder':'write something'}), max_length=4000, help_text='max words count 4000')

	class Meta:
		model = Topic
		fields =['subject', 'message']



class ReplyForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message']