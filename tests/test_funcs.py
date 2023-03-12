import pytest

from utils import utils


def test_json_get():
    URL = utils.URL
    assert utils.json_get(URL)


def test_empty_json_dict():
    testing_data = [{}, {1: 'a', 2: 'b', 3: 'c'}]
    desired_result = [{1: 'a', 2: 'b', 3: 'c'}]
    assert utils.check_dict(testing_data) == desired_result


def test_sort_by_time():
    testing_data = [{'date': '2017.05.11.'}, {'date': '2019.04.05.'}, {'date': '2016.01.04'}]
    desired_result = [{'date': '2019.04.05.'}, {'date': '2017.05.11.'}, {'date': '2016.01.04'}]
    assert utils.sort_by_time(testing_data) == desired_result


def test_date_edit_normal():
    testing_data = {'date': '2019-12-08T22:46:21.935582'}
    desired_result = '08.12.2019'
    assert utils.date_edit(testing_data) == desired_result


def test_date_edit_exception():
    testing_data = {}
    desired_result = 'Ошибка при прочтении даты'
    assert utils.date_edit(testing_data) == desired_result


def test_beneficiary_account_editor_exceptions():
    with pytest.raises(AttributeError):
        utils.beneficiary_account_editor({})


def test_beneficiary_short_name_card():
    testing_data = {'to': 'Maestro 3806652527413662'}
    desired_result = 'Maestro **3662'
    assert utils.beneficiary_account_editor(testing_data) == desired_result


def test_beneficiary_long_name_card():
    testing_data = {'to': 'Visa Classic 1435442169918409'}
    desired_result = 'Visa Classic **8409'
    assert utils.beneficiary_account_editor(testing_data) == desired_result
