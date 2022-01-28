from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_206_PARTIAL_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from users.service import UserPaginator
from users.models import CustomUser
from users.serializers import DetailedUserSerializer, BasicUserSerializer


class PrivateViewSet(ModelViewSet):
    """
    list: Paginated list of short information about all users
    retrieve: Detailed information about user
    create: Create new user
    partial_update: Update information about user
    destroy: Delete user
    """

    queryset = CustomUser.objects.all()
    pagination_class = UserPaginator
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action in ("retrieve", "create", "partial_update"):
            serializer_class = DetailedUserSerializer
            return serializer_class
        else:
            serializer_class = BasicUserSerializer
            return serializer_class


# Not Generic viewset for more flexible customization

# class PrivateViewSet(ViewSet):
#     queryset = CustomUser.objects.all()

#     def list(self, request):
#         serializer = CustomUserSerializer(self.queryset, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)

#     def create(self, request):
#         serializer = CustomUserSerializer(data=request.data, detailed=True)
#         serializer.is_valid(raise_exception=True)
#         new_user = serializer.save()
#         if new_user:
#             return Response(status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk):
#         user = get_object_or_404(self.queryset, pk=pk)
#         serializer = CustomUserSerializer(user, detailed=True)
#         return Response(serializer.data, status=HTTP_200_OK)

#     def destroy(self, request, pk):
#         user = get_object_or_404(self.queryset, pk=pk)
#         user.delete()
#         return Response(status=HTTP_204_NO_CONTENT)

#     def partial_update(self, request, pk):
#         user = get_object_or_404(self.queryset, pk=pk)
#         serializer = CustomUserSerializer(instance=user, data=request.data, partial=True, detailed=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=HTTP_206_PARTIAL_CONTENT)
