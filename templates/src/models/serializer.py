from datetime import datetime
from sqlalchemy.inspection import inspect
import uuid

class Serializer(object):
    def str_if_object(self,value):
        if isinstance(value,uuid.UUID):
            return str(value) 
        elif isinstance(value,datetime):
            return value.strftime("%F")
        else:
            return value

    def serialize(self,remove_fields=None,select_fields=None):
        serialized =  {c: self.str_if_object(getattr(self, c)) for c in inspect(self).attrs.keys()}
        if remove_fields:
            [serialized.pop(field) for field in remove_fields]
        elif select_fields:
            [serialized.pop(field) for field in serialized.copy().keys() if field not in select_fields]
            
        return serialized
