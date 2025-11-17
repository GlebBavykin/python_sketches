from json import loads
from jsonpath_ng import jsonpath, parse
from pprint import pprint


raw_string = """[
    {
        "site": "https://www.gosuslugi.ru/",
        "accounts":
        [
            {
                "login": "79818905703",
                "old_password": "DbSZk9rdsg9m_02",
                "password": "D7i8y4sdgsTX2Cpsu_17",
                "two_factor_authentication":
                {
                    "is_set": false,
                    "type": null,
                    "resource": null
                }
            }
        ]
    },
    {
        "site": "https://github.com/",
        "accounts":
        [
            {
                "login": "gleb-92@yandex.ru",
                "old_password": "Fi0VCPsdgfDAw1a",
                "password": "WfZn7uXCsdgsdYnNA5hO10",
                "two_factor_authentication":
                {
                    "is_set": true,
                    "type": "code_sent_to_email",
                    "resource": "gleb-92@yandex.ru"
                }
            }
        ]
    },
    {
        "site": "https://yandex.ru/",
        "accounts":
        [
            {
                "login": "gleb-92@yandex.ru",
                "old_password": "Z4N31dsfgknZ",
                "password": "ATjz6bOgdrewgfr3BEuPp2R",
                "two_factor_authentication":
                {
                    "is_set": true,
                    "type": "a_call_to_your_phone",
                    "resource": "79818905703"
                }
            }
        ]
    }]"""

my_json = loads(raw_string)
pprint(my_json)



data = parse('$[*].accounts[*].two_factor_authentication.is_set')
ls = data.find(my_json)
password_list = [item.value for item in ls]
pprint(password_list)