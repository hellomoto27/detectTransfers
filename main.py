
import json

"""Transfer detector.

Given a list of withdrawals and desposits, detect the likely transfers amongst them.

A few notes:
- The same withdrawal or deposit cannot be used for multiple different transfers. If there's a case where a given withdrawal or deposit can be matched with multiple possible transfers, use the first occurrence in the list.
- A transfer can only be made between different wallets.

For example, given:
[
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3),  # 5.3 BTC was withdrawn out of 'wallet_id_1'
	('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3.2),  # 3.2 BTC was withdrawn out of 'wallet_id_1'
	('tx_id_3', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_2'
	('tx_id_4', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_3'
]

Expected output:
[
	('tx_id_1', 'tx_id_3'),
]

Add a few tests to verify your implementation works on a variety of input
"""
    
"""
Parameters:
    transactions: List of transactions in form of json strings
"""
def detect_transfers(transactions):
    """Detects transfers amongst the given transactions."""
    outList = list()
    inList = list()
    resultList = list()
    for x in transactions:
        dic = json.loads(x);
        if dic["action"] == "out":
            outList.append(dic)
        else:
            inList.append(dic)

    while bool(outList):
        x = outList.pop()
        for y in inList:
            if x["time"] == y["time"] and x["amount"] == y["amount"] and x["walletId"] != y["walletId"]:
                resultList.append((x["id"], y["id"]))
                inList.remove(y)



    return resultList

def tests():
    first = [
        '{ "id":"1", "walletId":1, "time":"2020-01-01 15:30:20 UTC", "action": "out", "amount": 5.3}',
        '{ "id":"2", "walletId":1, "time":"2020-01-03 12:05:25 UTC", "action": "out", "amount": 3.2}',
        '{ "id":"3", "walletId":2, "time":"2020-01-01 15:30:20 UTC", "action": "in", "amount": 5.3}',
        '{ "id":"4", "walletId":3, "time":"2020-01-01 15:30:20 UTC", "action": "in", "amount": 5.3}'
    ]

    second = [
        '{ "id":"1", "walletId":1, "time":"2020-01-01 15:30:20 UTC", "action": "out", "amount": 5.3}',
        '{ "id":"2", "walletId":1, "time":"2020-01-03 12:05:25 UTC", "action": "out", "amount": 3.2}',
        '{ "id":"3", "walletId":2, "time":"2020-01-01 15:30:20 UTC", "action": "in", "amount": 5.4}',
        '{ "id":"4", "walletId":3, "time":"2020-01-01 15:30:20 UTC", "action": "in", "amount": 5.5}'
    ]

    third = [
        '{ "id":"1", "walletId":1, "time":"2020-01-01 15:30:20 UTC", "action": "out", "amount": 5.3}',
        '{ "id":"2", "walletId":1, "time":"2020-01-03 12:05:25 UTC", "action": "out", "amount": 3.2}',
        '{ "id":"3", "walletId":2, "time":"2020-01-01 15:30:20 UTC", "action": "in", "amount": 5.3}',
        '{ "id":"4", "walletId":3, "time":"2020-01-03 12:05:25 UTC", "action": "in", "amount": 3.2}'
    ]

    result = detect_transfers(first)
    result2 = detect_transfers(second)
    result3 = detect_transfers(third)
    print("First Case: ")
    print("Expected: [(u'1',u'3')]")
    print("Output: ")
    print(result)
    print("Second Case: ")
    print("Expected: []")
    print("Output: ")
    print(result2)
    print("Third Case: ")
    print("Expected: [(u'2', u'4'), (u'1', u'3')]")
    print("Output: ")
    print(result3)

tests()