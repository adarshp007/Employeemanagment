from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from Employeemanagement.db import TimestampedModel

# Create your models here.

class User(AbstractUser, TimestampedModel):
    EMP = 0
    MNGR = 1
    
    USER_TYPE_CHOICES = (
        (EMP, 'Employee'),
        (MNGR, 'Manager')
      
    )
    email = models.EmailField(('email address'), unique=True)
    mobile = PhoneNumberField(null=False,
                              blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    user_type= models.PositiveSmallIntegerField(
        default=EMP, choices=USER_TYPE_CHOICES)
    salary = models.IntegerField(default=0)
    employee_code=models.CharField(max_length=50,null=True,blank=True,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])