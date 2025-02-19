def create_account(name, holder, account_holders=[]):
    account_holders.append(holder)
    return {
        "account":name,
        "name":holder,
        "account_holders":account_holders
    }


acc_1 = create_account("current", "Rolf")
acc_2 = create_account("savings", "Sam")
print(acc_1)
print(acc_2)

