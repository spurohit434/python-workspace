accounts = {
    "savings": 3095.50,
    "current": 2300.00
}

def add_balance(amount, acc_type) -> bool :
    accounts[acc_type] += amount
    return accounts[acc_type]

print(id(accounts))
print(add_balance(1000, "savings"))
print(id(accounts))