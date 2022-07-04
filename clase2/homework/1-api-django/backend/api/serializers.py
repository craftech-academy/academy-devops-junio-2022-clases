from rest_framework.serializers import ModelSerializer
from api.models import Recordatorio

class RecordatorioSerializer(ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = ['detalle']