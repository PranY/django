from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class Url(models.Model):

	url = models.CharField(max_length='100')
	short = models.CharField(max_length='100')
