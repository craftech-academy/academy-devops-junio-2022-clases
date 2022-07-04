
from rest_framework.viewsets import ModelViewSet
from api.serializers import RecordatorioSerializer
from api.models import Recordatorio


class ApiViewSet(ModelViewSet):
    serializer_class = RecordatorioSerializer
    queryset = Recordatorio.objects.all()