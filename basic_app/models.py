from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    # Creates relationship to User class
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Additional Attributes
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return str(self.user.username)



# Create your models here.
