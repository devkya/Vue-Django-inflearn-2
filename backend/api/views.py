from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView

from blog.models import Post
from taggit.models import Tag
from django.db.models import Count

from api.views_util import obj_to_post, prev_next_post, make_tag_cloud



# Create your views here.
class ApiPostLV(BaseListView):
    model = Post
    
    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postList = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=postList, safe=False, status=200)
    
    
class ApiPostDV(BaseDetailView):
    model = Post
    
    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        post['prev'], post['next'] = prev_next_post(obj)        
        return JsonResponse(data=post, safe=True, status=200)
    
    
class ApiTagCloudLV(BaseListView):
    queryset = Tag.objects.annotate(count=Count('post'))
    
    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        tagList = make_tag_cloud(qs)
        return JsonResponse(data=tagList, safe=False, status=200)