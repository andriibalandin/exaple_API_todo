from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Task(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['completed']

    def __str__(self):
        return self.title

    def get_absolure_url(self):
        return reverse('notes:task', args=[self.slug])
    
    def get_udate_url(self):
        return reverse('notes:task-update', args=[self.slug])
    
    def get_delete_url(self):
        return reverse('notes:task-delete', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Task.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)
        