from django.db import models


# Create a Blog Models


class Blog(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to='images/')


# Add the blog app to the settings, then 

# Create a migrations using run python manage.py makemigrations

# Migrate using python manage.py migrate

# Add to the admin from model using the below line
#from .models import Job
# Register your models here.

#admin.site.register(Job)

