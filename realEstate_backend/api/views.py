from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Residency, ContactMessage
from .serializers import ResidencySerializer, ContactMessageSerializer


# Get residencies from database
@api_view(['GET'])
def residency_list(request):
    residencies = Residency.objects.all()
    serializer = ResidencySerializer(residencies, many=True)
    return Response(serializer.data)


# Save contact message
@api_view(['POST'])
def contact_create(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Message sent successfully!"})
    return Response(serializer.errors, status=400)


# Health check
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Welcome to the RealEstate Django Backend!"})
