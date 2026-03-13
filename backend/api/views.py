from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class HomeViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "this model is running"})