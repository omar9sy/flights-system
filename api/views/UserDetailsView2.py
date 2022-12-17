from collections import OrderedDict

from dj_rest_auth.views import UserDetailsView
from rest_framework.response import Response


class UserDetailsView2(UserDetailsView):
    def patch(self, request, *args, **kwargs):
        data = request.data
        new_data = OrderedDict([(key, data[key]) for key in data if self.ok(data[key])])
        instance = self.get_object()
        print(new_data)
        serializer = self.get_serializer(instance, data=new_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # noinspection PyMethodMayBeStatic
    def ok(self, s):
        if type(s) is list:
            return len(s) > 0
        if s == "":
            return False
        return s is not None
