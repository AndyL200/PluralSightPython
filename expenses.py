expenses = [10.50, 8, 5, 15, 20, 5, 3]

summation = 0

for x in expenses:
    summation = summation + x

print('You spent $', sum, sep = '')



for i in range(0,14,2):
    print(i)

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense")))
total = sum(expenses)
print(total)