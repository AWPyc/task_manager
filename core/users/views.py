from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserDetailSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = UserDetailSerializer(
            request.user,
            context={"user": request.user}
        )

        return Response(serializer.data)
