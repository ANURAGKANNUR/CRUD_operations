from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student


@api_view(['GET','POST'])
def student_list(request):
    if request.method=='GET':
        data=Student.objects.all()
        serializer=StudentSerializer(data,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def update_student(request,pk):
    if request.method=='GET':
        data=Student.objects.get(pk=pk)
        serializer=StudentSerializer(data)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method=='DELETE':
        data=Student.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
