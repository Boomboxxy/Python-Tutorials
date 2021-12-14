from django.db import models

# Create your models here.
class Person(models.Model):
    main_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()


