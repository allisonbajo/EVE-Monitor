from __future__ import annotations

import json
from io import StringIO
from dataclasses import dataclass


json_data = StringIO("""{
    "acc1":{
        "email":"acc1@example.com",
        "password":"acc1",
        "name":"ACC1",
        "salary":1
    },
    "acc2":{
        "email":"acc2@example.com",
        "password":"acc2",
        "name":"ACC2",
        "salary":2,
        "someRandomKey": "string"
    }
}
""")


@dataclass
class Account:
    email: str
    password: str
    name: str
    salary: int

    @classmethod
    def from_json(cls, json_key):
        file = json.load(json_data)
        return cls(**file[json_key])


if __name__ == '__main__':
    print("Load the data")
    key = 'acc1'
    account = Account.from_json(key)
    print(account)

