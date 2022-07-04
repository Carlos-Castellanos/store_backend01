

from audioop import add


def run_test():
    print("test 1 -dictionaries")

    me = {
        "first": "Carlos",
        "last": "Lopez",
        "Age": 51,
        "hobbies": ["read", "travel"],
        "address": {
            "street": "colins",
            "number": "123",
            "city": "San Francisco",
            "state": "CA",
            "zip": "123"
        }
    }

    print(me)
    print(me["first"])
    print(me["hobbies"])

    # print full name
    print(me["first"] + " "+me["last"])

    # chang values
    print(me["Age"])
    me["Age"] = me["Age"] + 1
    print(me["Age"])

    # add new keys
    me["preferred_color"] = "black"
    print(me)

    # me.clear()
    # print(me)

    # read if exists a keys in the dictionaries
    if "middlename" in me:
        print(me["middlename"])
    else:
        print("error")
    # print the full address in a simple line
    _address = me["address"]
    print(_address)
    print(type(_address))
    print(
        f'{_address["street"]}, #{_address["number"]}, {_address["city"]}, {_address["state"]}, zip {_address["zip"]}')


run_test()
