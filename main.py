import utils.utils
from utils.utils import func, check_dict, sort_by_time, date_edit

data = func(utils.utils.URL)
data = check_dict(data)
data = sort_by_time(data, "date")
data = date_edit(data)
for i in data:
    print(i)
# a = date_edit(sort_by_time(check_dict(func(utils.utils.URL)), 'date'))
# print(type(a))