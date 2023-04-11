from django.db import models

from pereval.resourses import STATUS


class Users(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PerevalAdded(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True)
    winter_level = models.CharField(max_length=100)
    summer_level = models.CharField(max_length=100)
    autumn_level = models.CharField(max_length=100)
    spring_level = models.CharField(max_length=100)
    coord_id = models.ForeignKey('Coords', on_delete=models.CASCADE)
    images = models.ManyToManyField('PerevalImages')
    status = models.CharField(choices=STATUS, default='new', max_length=8)

    def __str__(self):
        return f"{self.title} or {self.beauty_title}"


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.latitude} {self.longitude} {self.height}"


class PerevalImages(models.Model):
    img = models.ImageField(upload_to='uploads/')
    image_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.image_name}"


class PerevalAreas(models.Model):
    id_parent = models.IntegerField()
    title = models.TextField()

    def __str__(self):
        return f"{self.title}"
