# Generated by Django 3.2.6 on 2021-08-14 11:41

from django.db import migrations
from .. import scrapping

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]
    def getJobDetails(apps,schema_editor):
        Job=apps.get_model('api','jobDetails')
        all_jobs=[]
        internshala_job=scrapping.get_internshala_details()
        talentrack_job=scrapping.get_talentrack_details()
        iim_job=scrapping.get_iimjobs_details()
        all_jobs=internshala_job+talentrack_job+iim_job
        for job in all_jobs:
            job=Job(site=job.site,name=job.name,company=job.company,location=job.location,details=job.details,start_date=job.start_date,deadline=job.deadline)
            job.save()
    operations = [
        migrations.RunPython(getJobDetails),
    ]
