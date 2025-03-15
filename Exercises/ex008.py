# Your Student ID: 220543603
# Your Name and Surname: Muhammed Elubeyid

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    
    print(" " * (n - i), end="")
    
    print("*" * (2 * i - 1))
## Second way 
for i in range(1,6):
    for j in range(i,6):
        print(end=' ')
    for j in range(1,i+ 1):
        print('*', end='')
    for j in range(1,i):
     print('*', end='')
    print()
