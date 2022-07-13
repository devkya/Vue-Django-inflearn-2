from ctypes.wintypes import tagMSG
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    description = models.CharField(verbose_name='DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField(verbose_name="CONTENT")
    create_dt = models.DateTimeField(verbose_name='CREATE DATE', auto_now_add=True)
    update_dt = models.DateTimeField(verbose_name='UPDATE DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
    def get_prev(self):
        return self.get_previous_by_update_dt()
    
    def get_next(self):
        return self.get_next_by_update_dt()
    