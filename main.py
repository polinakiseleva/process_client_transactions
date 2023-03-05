import utils.utils
from utils.utils import json_get, check_dict, sort_by_time, date_edit


def main():
    json_data = json_get(utils.utils.URL)
    sorted_data_list = check_dict(json_data)
    sorted_data_by_time = sort_by_time(sorted_data_list, "date")
    final_data = date_edit(sorted_data_by_time)
    for i in final_data:
        print(i)


if __name__ == '__main__':
    main()
