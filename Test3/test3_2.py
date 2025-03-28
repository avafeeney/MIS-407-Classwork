def fizzbuzz(num):
    # Return fizzbuzz if divisible by 3 & 5, fizz if divisible by 3, and buzz if divisible by 5
    if num % 5 == 0 and num % 3 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return ""

for i in range(1, 51):
    print(i, fizzbuzz(i))