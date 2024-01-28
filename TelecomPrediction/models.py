from django.db import models

# Create your models here.
class customerInfo(models.Model):
    Age = models.IntegerField();
    Tenure_in_Months = models.IntegerField();
    Offer = models.IntegerField();
    Internet_Type = models.IntegerField();
    Avg_Monthly_GB_Download = models.IntegerField();
    Unlimited_Data = models.IntegerField();
    Contract = models.IntegerField();
    Payment_Method = models.IntegerField();
    Monthly_Charge = models.IntegerField();
    Total_Extra_Data_Charges = models.IntegerField();
    prediction = models.CharField(max_length=10, default="Some String2");

