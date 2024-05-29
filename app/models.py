from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=99,primary_key=True)
    email=models.EmailField(default='avm@gmail.com')
    
    def __str__(self) -> str:
        return self.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    wpages=models.CharField(max_length=100,default='w1')
    
    def __str__(self) -> str:
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=99)
    
    def __str__(self) -> str:
        return self.author