from django.db import models

class Proposalmodel(models.Model):
    title=models.CharField(max_length=250)
    fname=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.CharField(max_length=250)
    userType=models.CharField(max_length=250)
    status=models.CharField(max_length=255)
    ptitle=models.CharField(max_length=250)
    pdesc=models.CharField(max_length=250)
    pwebsite=models.CharField(max_length=250)
    comment=models.CharField(max_length=250)
    reference=models.CharField(max_length=250)
    document=models.CharField(max_length=250)

    
    class Meta:
        db_table="proposals"

