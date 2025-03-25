# Your Student ID: 220543603
# Your Name and Surname: Muhammed Elubeyid
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

numbers.extend([11, 12, 13])
print("List after adding :", numbers)

print("The list length :", len(numbers))

numbers.pop(0) 
numbers.pop()   
print("List after removing the first and last elements:", numbers)

for x in range(len(numbers)- 1, -1, -1):
    if numbers[x]% 2!= 0:
        numbers.pop(x)
print(sorted(numbers))

