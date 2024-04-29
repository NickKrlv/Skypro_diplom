from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from edu.models import EduModel
from edu.serializers import EduSerializer


class EduModelAPIView(ListAPIView):
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer


class EduModelDetailAPIView(RetrieveAPIView):
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer


class EduModelCreateAPIView(CreateAPIView):
    serializer_class = EduSerializer


class EduModelUpdateAPIView(UpdateAPIView):
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer


class EduModelDestroyAPIView(DestroyAPIView):
    queryset = EduModel.objects.all()
