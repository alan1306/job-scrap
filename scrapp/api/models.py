from django.db import models

class jobDetails(models.Model):
    site=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    details=models.TextField()
    start_date=models.CharField(max_length=20)
    deadline=models.CharField(max_length=20)
class interestingUrl(models.Model):
    urls=models.TextField()
class nonInterestingUrls(models.Model):
    urls=models.TextField()