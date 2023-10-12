from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import Teacher, Student
from rest_framework.response import Response
from .serializers import TeacherSerializer, StudentSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework import mixins
from django_filters import rest_framework as filters



class TeacherAPIView(APIView):
    def get(self, request, format=None):
        teacher_objs = Teacher.teacher_objects.all()
        serializer = TeacherSerializer(teacher_objs, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request, format=None, *args, **kwargs):
        request_data = request.data
        serializer = TeacherSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TeacherDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            teacher_obj = Teacher.teacher_objects.get(pk=pk)
            return teacher_obj
        except Teacher.DoesNotExist as ex:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = TeacherSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        request_data = request.data
        serializer = TeacherSerializer(obj, request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            error = serializer.errors
            return Response(f"Xato malumotlar kritilgan "
                            f"{list(error.keys())[0]} {list(error.values())[0]}",
                            status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        obj = self.get_object(pk)
        request_data = request.data
        serializer = TeacherSerializer(obj, request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            error = serializer.errors
            return Response(f"Xato malumotlar kritilgan "
                            f"{list(error.keys())[0]} {list(error.values())[0]}",
                            status=status.HTTP_400_BAD_REQUEST)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
class StudentListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.RetrieveModelMixin,
                               generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['id',]
    # pagination_class = StandardResultsSetPagination
    # permission_classes = []


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentRetrieveAPIView(mixins.RetrieveModelMixin,
                               generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
