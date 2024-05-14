from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Service(models.Model):
    objects = None
    zone = models.ForeignKey(Zone, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class EducationalProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
