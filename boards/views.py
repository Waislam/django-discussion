from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

# Create your views here.
class BoadList(ListView):
	model = Board
	template_name='home/index.html'
	context_object_name='boards'
	

def topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	querysert = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1 )
	page=request.GET.get('page', 1)
	print(page)
	paginator=Paginator(querysert, 20)

	try:
		topics=paginator.page(page) #will give topics from current page
	except PageNotAnInteger:
		topics=paginator.page(1)#will give first page
	except EmptyPage:
		topics=paginator.page(paginator.num_pages)

	hmm=topics.number
	print(hmm)
	return render(request, 'home/topic.html',{'board':board, 'topics':topics})
	


@login_required
def newtopic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	
	if request.method=='POST':
		form = PostForm(request.POST)
		user = request.user # User.objects.first()
		if form.is_valid():
			topic = form.save(commit=False)
			topic.starter=user
			topic.board=board
			topic.save()
			post=Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=user)
			return redirect('boards:topic_post', pk=pk, topic_pk=topic.pk)
	else:
		form =PostForm()
	return render(request, 'home/newtopic.html', {'board':board, 'form':form})

def topic_post(request, pk, topic_pk):
	topic=get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	topic.views += 1
	topic.save()
	return render(request, 'home/topic_post.html', {'topic':topic})


@login_required
def reply_topic(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	if request.method == 'POST':
		form = ReplyForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.topic = topic
			post.created_by = request.user
			post.save()

			topic.last_updated=timezone.now()
			topic.save()
			return redirect('boards:topic_post', pk=pk, topic_pk=topic_pk)
	else:
		form = ReplyForm()
	return render(request, 'home/reply_topic.html', {'topic':topic, 'form': form })


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
	model = Post
	fields =('message',)
	template_name='home/edit_post.html'
	pk_url_kwarg='post_pk'
	context_object_name='post'

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(created_by=self.request.user)


	def form_valid(self, form):
		post =form.save(commit=False)
		post.uddated_by =self.request.user
		post.udapted_at = timezone.now()
		post.save()
		return redirect('boards:topic_post', pk=post.topic.board.pk, topic_pk=post.topic.pk)

