from django.db import models 

# Create your models here.
class students(models.Model):
    student_id = models.IntegerField(max_length = 100)
    name = models.CharField (max_length = 255)
    standerd = models.CharField (max_length = 50) 

    def __str__(self):
        return self.name