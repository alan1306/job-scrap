from django.contrib import admin
from .models import jobDetails,interestingUrl,nonInterestingUrls
# Register your models here.
admin.site.register(jobDetails)
admin.site.register(interestingUrl)
admin.site.register(nonInterestingUrls)