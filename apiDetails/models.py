from django.db import models
from django.db.migrations import Migration
import csv
# Create your models here.
from psycopg2.sql import NULL


class Bankings_info(models.Model):

    id=models.AutoField(primary_key=True, unique=True)
    ifsc = models.CharField(max_length=50)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=60)
    district = models.CharField(max_length=60)

    def __str__(self):
                return self.id +" : "+ self.ifsc
