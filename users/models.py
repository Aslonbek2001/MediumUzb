from django.db import models
from django.contrib.auth.models import AbstractUser
from utility.models import Utility

class User(Utility, AbstractUser):
    RULES = (
        ('ordinary', 'Ordinary'),
        ('author', 'Author'),
        ('admin', 'Admin'),
    )
    rule = models.CharField(
        max_length=10,
        choices=RULES,
        default='ordinary', 
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    experience = models.PositiveIntegerField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)
    youtube_link = models.URLField(max_length=200, null=True, blank=True)
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)
    own_website = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


