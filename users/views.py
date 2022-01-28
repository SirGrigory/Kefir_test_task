from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from .service import UserPaginator, UserUpdatePermission
from .models import CustomUser
from .serializers import DetailedUserSerializer, BasicUserSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    list: Paginated list of short information about all users available for current user
    retrieve: Available information about any user
    partial_update: Update information about current user
    """

    queryset = CustomUser.objects.all()
    pagination_class = UserPaginator
    serializer_class = BasicUserSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = BasicUserSerializer
        if self.action in ("retrieve", "partial_update"):
            serializer_class = DetailedUserSerializer
            kwargs.setdefault("private", False)
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_permissions(self):
        if self.action in ("retrieve",):
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (UserUpdatePermission,)
        return [permission() for permission in permission_classes]

    def retrieve(self, request):
        user = request.user
        serializer = DetailedUserSerializer(instance=user, private=False)
        return Response(serializer.data, status=HTTP_200_OK)
