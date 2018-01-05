from django.conf.urls import url
from . import views


# Regular expression masks for entities in URLs
BLOG_RE = r'(?P<blog_name>[a-zA-Z_]+)'
POST_RE = r'(?P<post_id>\d+)'
POST_SLUG_RE = r'(?P<post_id>\d+)-(?P<slug>[-\d\w]+)'
COMMENT_RE = r'(?P<comment_id>\d+)'

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^' + BLOG_RE + r'/$', views.blog_posts, name='blog_posts'),
    url(r'^' + BLOG_RE + r'/contribute/start/$', views.blog_add_contributor, name='blog_add_contributor'),
    url(r'^' + BLOG_RE + r'/contribute/stop/$', views.blog_remove_contributor, name='blog_remove_contributor'),
    url(r'^' + BLOG_RE + r'/new/$', views.add_new_post, name='add_new_post'),
    url(r'^' + BLOG_RE + r'/' + POST_RE + r'/$', views.get_post, name='get_post'),  # Accepts raw post_id
    url(r'^' + BLOG_RE + r'/' + POST_SLUG_RE + r'/$', views.get_post, name='get_post'),  # and any slug sequence (redirects to canonical)
    url(r'^' + BLOG_RE + r'/' + POST_SLUG_RE + r'/edit/$', views.edit_post, name='edit_post'),
    url(r'^' + BLOG_RE + r'/' + POST_SLUG_RE + r'/delete/$', views.delete_post, name='delete_post'),
    url(r'^' + BLOG_RE + r'/' + POST_SLUG_RE + r'/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^post/' + POST_SLUG_RE + r'/repost/$', views.repost, name='repost'),
    url(r'^post/' + POST_SLUG_RE + r'/rate/(?P<rating_sign>plus|minus)/$', views.rate_post, name='rate_post'),
    url(r'^comment/' + COMMENT_RE + r'/rate/(?P<rating_sign>plus|minus)/$', views.rate_comment, name='rate_comment'),
]
