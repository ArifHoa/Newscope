from django.db import models

class Casterm(models.Model):
    GENDER=(
        ('','Select Gender'),
        ('Male','Male'),
        ('Famale','Famale')
    )
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profel',blank=True,null=True)
    gender = models.CharField(max_length=16,choices=GENDER)
    def __str__(self):
        return f'{self.name}_{self.role}_{self.gender}'
