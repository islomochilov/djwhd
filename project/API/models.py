from django.db import models

# Create your models here.




class Contact(models.Model):
    full_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    phone_number=models.CharField(max_length=120)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
