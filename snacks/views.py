from rest_framework import generics
from .serializers import SnackSerializer
from .models import Snack


# Create your views here.
class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
