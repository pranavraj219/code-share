from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    lang_choices = (
    ('text', 'Plain Text'),
    ('c_cpp', 'C++'),
    ('java', 'Java')
    )
    title = models.CharField(max_length=200)
    src_lang = models.CharField(blank=True,default='txt', max_length=100, choices=lang_choices)
    src_code = models.CharField(max_length=50000)
    pwd = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("submit_code")
