from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


class UpdateDestroyView(GenericAPIView,
                        DestroyModelMixin,
                        UpdateModelMixin):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)