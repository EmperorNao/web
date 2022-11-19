from django.db import models


class Service(models.Model):

    title = models.CharField(max_length=30)
    image = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):

    text = models.TextField()

    def __str__(self):
        return self.text[:20]


class Contact(models.Model):

    image = models.ImageField()
    fullname = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Link(models.Model):
    logo = models.ImageField()
    url = models.CharField(max_length=30)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
