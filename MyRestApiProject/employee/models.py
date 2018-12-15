from django.db import models

class employees(models.Model):

    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    # email_id =models.EmailField(max_length=20)
    # emp_mobile_number=models.IntegerField()
    # emp_dob=models.DateField()


    def __str__(self):
        return self.firstname
