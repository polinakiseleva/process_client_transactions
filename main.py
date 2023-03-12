from utils import utils


def main():
    json_data = utils.json_get(utils.URL)
    sorted_data_list = utils.check_dict(json_data)
    sorted_data_by_time = utils.sort_by_time(sorted_data_list, "date")
    final_data = utils.output_of_the_last_transactions(sorted_data_by_time)

    for i in final_data:
        print(f'{utils.date_edit(i)} {i["description"]}\n'
              f'{utils.users_account_edit(i)} -> {utils.beneficiary_account_editor(i)}\n'
              f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n')


if __name__ == '__main__':
    main()
