from rest_framework import serializers
from .models import Company
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
        # fields=