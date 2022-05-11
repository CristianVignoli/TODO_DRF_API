from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, filters
from rest_framework.response import Response
from .serializers import RegistrationSerializer, TODOItemSerializer


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user': serializer.data})


class TODOViewSet(viewsets.ModelViewSet):
    serializer_class = TODOItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'creation_date']

    def get_queryset(self):
        return self.request.user.todo_list.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TODOItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TODOItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.todo_list.filter(
            pk=self.request.parser_context['kwargs']['pk']
        )