from django.db import models
import os
import random
from django.utils import timezone
from django.contrib.auth.models import User, Group


def content_file_name(instance, filename):
    now = timezone.now()
    x = str(now).replace("-", "").replace(" ", "").replace(":",  "").replace("+", "").replace(".", "")
    ext = filename.split('.')[-1]
    name = random.randint(100, 99999)
    filename = "%s%s.%s" % (x, name, ext)
    return os.path.join(filename)


class Profile(models.Model):
	list_choice_type = (
	    ("paid", "Paid"),
	    ("referral", "Referral"),
	)

	user = models.ForeignKey(User, related_name="user_profile", null=True)
	fullname = models.CharField(max_length=255, blank=True, null=True)
	avatar = models.ImageField(upload_to=content_file_name, default='avt.png', blank=True, null=True)
	phone = models.IntegerField(blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	invite = models.IntegerField(default=0)
	type_account = models.CharField(max_length=9, choices=list_choice_type, default="buy")
	token = models.CharField(max_length=255, blank=True, null=True)
	updated_by = models.ForeignKey(User, related_name='blog_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='blog_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.fullname
