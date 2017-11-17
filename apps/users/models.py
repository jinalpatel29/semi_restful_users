# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def basic_validator(self, postdata):
        print postdata
        errors = {}
        if len(postdata['fname']) < 2:
            errors["fname"] = "User first_name should be more than 2 characters"
        if len(postdata['lname']) < 2:
            errors["lname"] = "User last_name should be more than 2 characters"
        if postdata['email'] != "":
            if not EMAIL_REGEX.match(postdata['email']):
                errors["email_id"] = "Invalid Email Address! please follow abc@xyz.com"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_id = models.CharField(max_length = 255)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()