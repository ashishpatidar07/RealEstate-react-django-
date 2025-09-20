from rest_framework import serializers
from .models import Residency
from .models import ContactMessage

class ResidencySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # important!

    class Meta:
        model = Residency
        fields = '__all__'




class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
# from rest_framework import serializers
# from .models import Residency, ContactMessage