from django.db import models
import uuid
# Create your models here.


class Parking(models.Model):

    parking_id = models.CharField(primary_key=True,max_length=100,default=uuid.uuid1)
    parking_name = models.CharField(max_length=32,null=True,db_index=True)
    updated_time = models.DateTimeField(auto_now=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True,db_index=True,null=True)

    company = models.ForeignKey(

        'company.Company',
        related_name='parking_company',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'parking'
