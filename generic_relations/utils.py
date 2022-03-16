from collections import UserDict
from django.utils.module_loading import import_string

class ModelSerializerMap(UserDict): # Ideally dict should be subclassed

    def __getitem__(self, item):
        return {k: import_string(v)() for k, v in self.data.items()}.get(item,None)
