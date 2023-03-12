import utils.utils
from utils.utils import json_get, check_dict, sort_by_time, output_of_the_last_transactions


def main():
    json_data = json_get(utils.utils.URL)
    sorted_data_list = check_dict(json_data)
    sorted_data_by_time = sort_by_time(sorted_data_list, "date")
    output_of_the_last_transactions(sorted_data_by_time)


if __name__ == '__main__':
    main()
