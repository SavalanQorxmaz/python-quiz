
from utils import f_make_data

data = f_make_data()

if data:
    [[print(x) for x in d.items() ] for d in data]