from collections import UserDict
from django.utils.module_loading import import_string

class ModelSerializerMap(UserDict): 
    """\
    Mapping model classes to serializer classes
    
    This dictionery is instantiated with the import paths for one or more model(s) for the keys and the preferred serializer for each model as the value(s).
    When a key is later accessed the instantiated serializer is returned in place of its input path. ::
    
        ModelSerializerMap{"APP.models.MODEL":"APP.serializers.SERIALIZER"}["APP.models.MODEL"] => APP.serializers.SERIALIZER()
    """
    # Ideally dict should be subclassed

    def __getitem__(self, item):
        return {k: import_string(v)() for k, v in self.data.items()}.get(item,None)
