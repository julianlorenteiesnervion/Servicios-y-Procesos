def isPrime(number):
    divisors = 0

    for i in range(1, number + 1):
        if number % i == 0:
            divisors += 1
    
    return divisors == 2

number = int(input("Introduce un número: "))

print(f"El número {number} {'es' if isPrime(number) else 'no es'} primo.")