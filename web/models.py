from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.CharField(max_length = 100)
    company = models.ForeignKey(Company,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    request = models.TextField()
    create_at = models.DateTimeField(auto_now = True) 
    is_active = models.BooleanField()

class Applications(models.Model):
    vacancy = models.ForeignKey(Vacancy,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    cv = models.FileField(null=True)
    info = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()           
