# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Model to set the bank accounts
class Account(models.Model):
    account_name = models.CharField(max_length=100)
    intial_balance = models.DecimalField(max_digits=100, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.account_name
    
# Model to set the Budgets based 
class Budget(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name