# AUTHENTICATION
from django.contrib.auth import authenticate, get_user_model, login, logout

# USER MODEL
from django.contrib.auth.models import User, UserManager, BaseUserManager, AbstractUser, AbstractBaseUser

# COLLECTION
from collections import OrderedDict

# FORMS
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# TOKEN GENERATOR
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# GET CURRENT SITE
from django.contrib.sites.shortcuts import get_current_site

# EMAIL BACKENDS
from django.core.mail import EmailMultiAlternatives

# REVERSE LAZY
from django.utils.translation import ugettext, ugettext_lazy as _
from django.urls import reverse


# CLASS BASED VIEW
from django.views.generic import View   # Base view
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from django.views.generic.edit import FormView 


# HTTP RESPONSE
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# SHORTCUTS
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect



# TIMEZONE
from django.utils import timezone



# LOGIN REQUIRED DECORATOR
from django.contrib.auth.decorators import login_required

# URL PATH CONF
from django.urls import path

# ADMIN 
from django.contrib import admin

# DATABASE MODELS
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE) # foreign key
    toppings = models.ManyToManyField(Topping) # Many-to-many

    release_date = models.DateField()
    num_stars = models.IntegerField()
    article_id = models.AutoField(primary_key=True)
    data = models.JSONField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    email = models.EmailField()
    serves_hot_dogs = models.BooleanField(default=False)

    data={
      'breed': 'labrador',
      'owner': {
          'name': 'Bob',
          'other_pets': [{
              'name': 'Fishy',
          }],
      },
  }



    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

# CHOICE FIELDS
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),      # (db, user)
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
    school_name = models.CharField(max_length=1, choices=YEAR_IN_SCHOOL_CHOICES)


# Q objects
from django.db.models import Q

# OBJECT DOES NOT EXISTS
from django.core.exceptions import ObjectDoesNotExist



changes-made---BRANCH-S01

changes by me (Gaurav girase)
this changes has been made by master baranch we need 

i am mater---changes-1
i am mater---changes-2


