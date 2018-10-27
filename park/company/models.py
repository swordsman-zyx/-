from django.db import models
import uuid
# Create your models here.


class Company(models.Model):

    company_id = models.CharField(primary_key=True,max_length=100,default=uuid.uuid1)
    company_name = models.CharField(max_length=32,null=True,db_index=True)
    updated_time = models.DateTimeField(auto_now=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True,db_index=True,null=True)

    class Meta:

        db_table = 'company'
