from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import NumberSet
from .serializer import NumberSetSerializer

# Create your views here.
number_set = NumberSet()

class ExtractNumberView(APIView):
    def post(self, request):
        serializer = NumberSetSerializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data['number']
            try:
                number_set.extract(number)
                missing_number = number_set.calculate_missing()
                return Response(
                    {"message": f"El número faltante es {missing_number}."},
                    status=status.HTTP_200_OK
                )
            except ValueError as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)