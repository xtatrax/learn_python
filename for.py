# !/bin/bash python3
# -*- coding: utf-8 -*-

arrayDic = [
    {
        "id":1,
        "data":"John Doe"
    },
    {
        "id":2,
        "data":"Jane Doe"
    }
]

dicDic = {
    "John Doe":{
        "id":1,
        "data":"John Doe"
    },
    "Jane Doe":{
        "id":2,
        "data":"Jane Doe"
    }
}

for d in arrayDic:
    print(d)


for d in dicDic:
    print(d)