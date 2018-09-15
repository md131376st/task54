from django.db import models
# the file field we save are csv files in database 
class CsvDoc(models.Model):
    csv_file = models.FileField(upload_to='csv/%Y/%m/%d')
    def __str__(self):
        return self.csv_file.name
# Create your models here.
