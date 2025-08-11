from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import process_image_service

@api_view(['POST'])
def process_image_view(request):
    if 'image' not in request.FILES:
        return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

    result = process_image_service(request.FILES['image'])
    
    if result.get("error"):
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return HttpResponse(result["image_bytes"], content_type="image/png")
