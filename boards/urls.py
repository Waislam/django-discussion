from django.urls import path
from .views import BoadList, topic, newtopic, topic_post, reply_topic, PostUpdateView

app_name ='boards'

urlpatterns =[
	path('', BoadList.as_view(), name='home'),
	path('topic/<int:pk>/', topic, name='topic'),
	path('topic/<int:pk>/new/', newtopic, name='new'),
	path('boards/<int:pk>/topics/<int:topic_pk>/', topic_post, name='topic_post' ),
	path('boards/<int:pk>/topics/<int:topic_pk>/reply', reply_topic, name='reply' ),
	path('boards/<int:pk>/topics/<int:topic_pk>/post/<int:post_pk>/edit/', PostUpdateView.as_view(), name='edit_post' ),

]