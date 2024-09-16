from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework import mixins
from rest_framework.response import Response
from app.common.utils import get_response
from app.errors.services import trigger_rest_not_found


class MyDestroyModelMixin(mixins.DestroyModelMixin):
    def set_object_non_active(self, instance):
        instance.is_active = False
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            if instance.company_id != request.user.company_id:
                raise NotFound
        except NotFound:
            raise NotFound
        except:
            pass
        self.set_object_non_active(instance)
        return Response(get_response([]))

class MyUpdateModelMixin(mixins.UpdateModelMixin):
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

class MyPartialUpdateModelMixin(mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')