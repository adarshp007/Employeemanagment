from rest_framework import serializers
from employee.models import (User)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields =[
            'id',
            'employee_code',
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'mobile',
            'salary'
        ]
