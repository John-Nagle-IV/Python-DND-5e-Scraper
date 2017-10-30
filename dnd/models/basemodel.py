import json

class BaseModel(object):
    MODEL_ATTRIBUTES = []
    def __init__(self, *args, **kwargs):
        for attr, index in enumerate(self.MODEL_ATTRIBUTES):
            setattr(self, self.MODEL_ATTRIBUTES[index], attr)

        for attr, val in kwargs.items():
            setattr(self, attr, val)
