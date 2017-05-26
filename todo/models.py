from django.db import models
from todoapp import settings


# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=30)
    createTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    todoAmount = models.IntegerField(default=0)
    finishedAmount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def incomplete_tasks(self):
        # Count all incomplete tasks on the current list instance
        return Item.objects.filter(list=self, completed=0)

    def get_absolute_url(self):
        return "/list/%s/" %(self.id)


class Item(models.Model):
    title = models.CharField(max_length=30)
    createTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    due_Date = models.DateTimeField(blank=False, )
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    list = models.ForeignKey(List)
    
    
    def __str__(self):
        return self.title

