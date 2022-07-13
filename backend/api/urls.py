from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),
    path('tag/cloud/', views.ApiTagCloudLV.as_view(), name='ta_cloud'),
]
