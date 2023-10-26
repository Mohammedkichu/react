from medicine.models import Medicine
from rest_framework import serializers

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('mname', 'description', 'side_effect', 'expiry_date','Price')

