# Exercise #2
# Get first prime numbers up to 100
for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            break