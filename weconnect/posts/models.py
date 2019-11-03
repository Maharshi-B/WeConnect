from django.db import models
from django.urls import reverse
from django.conf import settings
import mistune
from groups.models import Group
from django.contrib.auth import get_user_model
# Create your models here.
# Posts models.py
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',  on_delete="Cascade")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',  on_delete="Cascade",
                              null=True, blank=False)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = mistune.markdown(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',
                       kwargs={'pk': self.pk, })

    class Meta():
        ordering = ['-created_at']
        unique_together = ['user', 'created_at']
