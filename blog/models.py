from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
  #  text = models.TextField()
    text = HTMLField() 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    header_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
#kode sebelumnya
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text

#jawaban no 3.12 about pada blog
from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError("Hanya boleh ada satu halaman About")
        return super().save(*args, **kwargs)

