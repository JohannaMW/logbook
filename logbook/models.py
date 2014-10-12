from django.db import models
from django.contrib.auth.models import User
import urllib
import json
from django.db import models
from django_boto.s3.storage import S3Storage


class Journey(models.Model):
    main_image = models.ImageField(upload_to='photos', blank=True, null=True)
    image_1 = models.ImageField(upload_to='photos', blank=True, null=True)
    image_2 = models.ImageField(upload_to='photos', blank=True, null=True)
    image_3 = models.ImageField(upload_to='photos', blank=True, null=True)
    image_4 = models.ImageField(upload_to='photos', blank=True, null=True)
    image_5 = models.ImageField(upload_to='photos', blank=True, null=True)
    summary = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=400)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="journeys")
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    marker_symbol = models.CharField(max_length=20, blank=True, null=True)
    marker_color = models.CharField(max_length=20, blank=True, null=True)

    def save(self):
        location = "{}, {}".format(self.city, self.country)

        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.geocode(location)

        super(Journey, self).save()

    def geocode(self, location):
        location = urllib.quote_plus(location)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return latitude, longitude

