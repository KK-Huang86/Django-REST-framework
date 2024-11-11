from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = (JSONParser,)

    # permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    # [GET] api/shares/
    def list(self, request, **kwargs):
        users = Book.objects.all()
        serializer = BookSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # [POST] api/shares/
    @permission_classes([IsAuthenticated])
    def create(self, request, **kwargs):
        name = request.data.get("name")
        users = Book.objects.create(name=name)
        serializer = BookSerializer(users)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
