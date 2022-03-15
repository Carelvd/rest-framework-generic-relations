from collections import UserDict
from django.utils.module_loading import import_string

class ModelSerializerMap(UserDict): # Ideally dict should be subclassed

    def __getitem__(self, item):
        # print(item in self.data)
        # print(item, self.data.items())
        # print({import_string(k): import_string(v)() for k, v in self.data.items()})
        # print(item in (import_string(k) for k in self.data.keys()), [import_string(k) for k in self.data.keys()])
        return {k: import_string(v)() for k, v in self.data.items()}.get(item,None)
