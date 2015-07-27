from rest_framework import viewsets

from .models import Accounts, History
from .serializers import AccountSerializer, HistorySerializer

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
