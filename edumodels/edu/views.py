from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from edu.models import EduModel
from edu.pagination import MyPagination
from edu.permissions import IsAdmin
from edu.serializers import EduSerializer


class EduModelAPIView(ListAPIView):
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class EduModelDetailAPIView(RetrieveAPIView):
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer
    permission_classes = [AllowAny]


class EduModelCreateAPIView(CreateAPIView):
    serializer_class = EduSerializer
    permission_classes = [IsAuthenticated]


class EduModelUpdateAPIView(UpdateAPIView):
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer
    permission_classes = [IsAuthenticated]


class EduModelDestroyAPIView(DestroyAPIView):
    queryset = EduModel.objects.all()
    permission_classes = [IsAdmin]
