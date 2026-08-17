#Print 1 to n numbers
for i in range(10):
    print(i)
#2. Write a program to Print REVERSE of N to 1 numbers? 
for i in range(10,0,-1):
    print(i)
#3. Write a program to display sum of 1 to N numbers? 
sum = 0
for i in range(10):
    sum +=i
    print(sum)

#4. Write a program to check given number is EVEN or ODD? 
for i in range(100):
    if i % 2 ==0:
       print(i,"Even")
    else:
        print(i,"Odd")
#5. Write a program to display PRIME NUMBERS from 1 to n? 
for i in range(2, 20):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i, "Prime")
#6.Sum Of All the prime Numbers
sum = 0

for i in range(2, 20):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        sum += i
        print(i, "Prime")

print("Sum =", sum)

#7Write a program to display MULTIPLICATION table? 
n = 2
for i in range(11):
    result=n*i
    print(result)