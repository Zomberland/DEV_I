from services.serializers import ReporterMinimalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from relacionamentos.models import Reporter

class ReporterListService(APIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterMinimalSerializer

    def get(self,request, format=None):
        reporters = Reporter.objects.all()
        context = {
            'request': request,
            'format': format,
        }
        serializer = ReporterMinimalSerializer(reporters, many=True, context=context)

        return Response(serializer.data)

    def post(self, request, format=None):
        dados = resquest.data
        context = {
            'request': request,
            'format': format,
        }

        serializer = ReporterMinimalSerializer(data=dados, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
