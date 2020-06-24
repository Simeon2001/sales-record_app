from django.db import models


class Sales(models.Model):
    client = models.CharField(max_length=15)
    end_user = models.CharField(max_length=15)
    description = models.CharField(max_length=15)
    model_serial_no = models.CharField(max_length=15)
    qty = models.IntegerField()
    gate_pass = models.CharField(max_length=15)
    category = models.CharField(max_length=25)
    sales_date = models.DateField()
    
    def __str__(self):
        return self.client

    #class Meta:
        #db_table = "tbl_sales"



