import pathlib
import os
import json


DATA = json.load(open(os.path.join(pathlib.Path(__file__).parent, 'data.json'), 'r+b'))['data']
