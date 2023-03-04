import requests

URL = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678006423443&signature=LrRvgBmzJUjZRcDynWElQuoPThOTcQ7TWHsT_dTyv0I&downloadName=operations.json'


def func(par):
    responce = requests.get(par)
    return responce.json()


def check_dict(list_data):
    list1 = []
    for i in list_data:
        if len(dict) != 0:
            list1.append(dict)
        else:
            continue
