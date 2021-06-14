from server.models import Video
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import VideoSerializer

# Create your views here.

def all(request):
    data = Video.objects.all().values()
    data_list = list(data)
    return JsonResponse(data_list, safe=False)

def item(request, id):
    data = Video.objects.filter(id=id).values()
    data_list = list(data)
    return JsonResponse(data_list, safe=False)

@api_view(['POST'])
def post(request):
    data = VideoSerializer(data=request.data)

    if data.is_valid():
        data.save()

    return Response(data.data)