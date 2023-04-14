from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    comment = models.TextField(max_length=1000)
    post = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Price(models.Model):
class Information(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Qualifications(models.Model):
    title = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SkillRight(models.Model):
    title   = models.CharField(max_length=100)

    def __str__(self):
        return self.title