from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class ClientTrainer(models.Model):
    client = models.ForeignKey(User, related_name='client', null=True,blank=True,on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, related_name='trainer', null=True,blank=True,on_delete=models.CASCADE)

class ForumPost(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)

class ForumReply(models.Model):
    comment = models.ForeignKey(ForumPost, null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)

class TrainerReview(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)

class TrainerBlog(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)

class Workout(models.Model):
    user = models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    notes = models.CharField(max_length=1000,null=True,blank=True)
    #day1
    day1ex1 = models.CharField(max_length=50,null=True)
    day1ex1sets = models.IntegerField(null=0)
    day1ex1reps = models.IntegerField(null=0)
    day1ex2 = models.CharField(max_length=50,null=True)
    day1ex2reps = models.IntegerField(null=0)
    day1ex2sets = models.IntegerField(null=0)
    day1ex3 = models.CharField(max_length=50,null=True)
    day1ex3sets = models.IntegerField(null=0)
    day1ex3reps = models.IntegerField(null=0)
    day1ex4 = models.CharField(max_length=50,null=True)
    day1ex4sets = models.IntegerField(null=0)
    day1ex4reps = models.IntegerField(null=0)
    #day2
    day2ex1 = models.CharField(max_length=50,null=True)
    day2ex1sets = models.IntegerField(null=0)
    day2ex1reps = models.IntegerField(null=0)
    day2ex2 = models.CharField(max_length=50,null=True)
    day2ex2reps = models.IntegerField(null=0)
    day2ex2sets = models.IntegerField(null=0)
    day2ex3 = models.CharField(max_length=50,null=True)
    day2ex3sets = models.IntegerField(null=0)
    day2ex3reps = models.IntegerField(null=0)
    day2ex4 = models.CharField(max_length=50,null=True)
    day2ex4sets = models.IntegerField(null=0)
    day2ex4reps = models.IntegerField(null=0)
    #day3
    day3ex1 = models.CharField(max_length=50,null=True)
    day3ex1sets = models.IntegerField(null=0)
    day3ex1reps = models.IntegerField(null=0)
    day3ex2 = models.CharField(max_length=50,null=True)
    day3ex2reps = models.IntegerField(null=0)
    day3ex2sets = models.IntegerField(null=0)
    day3ex3 = models.CharField(max_length=50,null=True)
    day3ex3sets = models.IntegerField(null=0)
    day3ex3reps = models.IntegerField(null=0)
    day3ex4 = models.CharField(max_length=50,null=True)
    day3ex4sets = models.IntegerField(null=0)
    day3ex4reps = models.IntegerField(null=0)


