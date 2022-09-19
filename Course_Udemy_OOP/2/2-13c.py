class Bank:
    apr =1.2

print(Bank.__dict__)

acc1 = Bank()
acc2 = Bank()

acc1 is acc2 # False

print(acc1.apr, acc2.apr)

Bank.acc_type = "Savings"
print(acc1.__dict__, acc2.__dict__)

acc1.apr = 0

print('*' * 30)

print(acc1.__dict__, acc2.__dict__)#acc2.apr =1.2
print(Bank.__dict__)  # means pyhton looks into instance dict and if not found go to parent dict


acc1.bank = "Saving and loans"
print(acc1.__dict__, acc2.__dict__)

