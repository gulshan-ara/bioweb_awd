from django.db import models

#  demo model with only a field named text
class Hello(models.Model):
  text = models.CharField(max_length=200)