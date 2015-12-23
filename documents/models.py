from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
  user = models.ForeignKey(User)
  pub_date = models.DateTimeField('date published')
  text = models.CharField(max_length=20000)
  title = models.CharField(max_length=100)
  sub_title = models.CharField(max_length=100)
  domain = models.CharField(max_length=50)
