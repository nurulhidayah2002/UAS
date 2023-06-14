from django.db import models

class barang(models.Model):
  firstname = models.CharField(max_length=15)
  lastname = models.CharField(max_length=15)