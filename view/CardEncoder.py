import json
from json import JSONEncoder

class CardEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__