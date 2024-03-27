from rest_framework import serializers
from .models import Company,Employee
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields='__all__'
        # fields=
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__'