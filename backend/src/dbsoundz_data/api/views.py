from rest_framework.generics import ListAPIView, RetrieveAPIView
from dbsoundz_data.models import Data
from .serialzers import DataSerializer


class DataListView(ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataDetailView(RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
