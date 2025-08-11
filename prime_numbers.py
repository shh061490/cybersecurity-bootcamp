
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [3, 4, 5, 6, 7]
print([num for num in numbers if is_prime(num)])