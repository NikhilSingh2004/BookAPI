from api.models import User
from rest_framework import generics
from api.serializers import BookSerializer
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.books.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
