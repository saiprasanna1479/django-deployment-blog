from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey('blog.post',related_name="comments",on_delete=models.CASCADE)
    author=models.CharField(max_length=256)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approve_comment=models.BooleanField(default=False)

    def approve(self):
        self.approve_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
