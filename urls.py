from django.conf.urls import url
from . import views

app_name = 'blog'


urlpatterns = [
    
     url(r'^$', views.PostListView.as_view(),name='post_list'),
     url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
     url(r'^post/create/$', views.CreatePostView.as_view(),name='post_create'),
     url(r'^post/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(),name='post_update'),
     url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(),name='post_delete'),
     url(r'^drafts/$', views.DraftListView.as_view(),name='post_draft_list'),
     url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment,name='add_comment'),
     url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve,name='comment_approve'),
     url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,name='comment_remove'),
     url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish,name='post_publish'),
]