from django.db import models
from django.contrib.auth.models import User

from sphene.community.models import Group

# Create your models here.

class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(maxlength = 250)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name;

    class Admin:
        pass

class TrackerItem(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(maxlength = 250)
    author = models.ForeignKey(User, related_name = 'tracker_item_author')
    owner = models.ForeignKey(User, related_name = 'tracker_item_owner')
    postdate = models.DateTimeField( auto_now_add = True )
    description = models.TextField(blank = True)

    def __str__(self):
        return self.title;

    class Admin:
        pass


class TimeEntry(models.Model):
    owner = models.ForeignKey(User)
    trackerItem = models.ForeignKey(TrackerItem)
    postdate = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.description;

    class Admin:
        pass
