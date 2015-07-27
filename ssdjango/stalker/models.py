from django.db import models

# Create your models here.

class Accounts(models.Model):
    """
    Model for User Accounts signing into Stock Stalker Application
    """
    user_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user_id


class History(models.Model):
    """
    Model for storing user stock search history
    """
    user_id = models.CharField(max_length=200)
    search = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user_id
