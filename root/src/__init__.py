def primes(a, b):
    """
    returns list of prime numbers between a and b included
    """

    primes = [2]

    if a < 2:
        a = 2

    for number in range(3, b + 1):
        b = 1
        for num in primes:
            if number % num == 0:
                b = 0
                break
        if b == 1:
            primes.append(number)

    index = 0
    while primes[index] < a and index < len(primes) - 1:
        index += 1

    return [] if index == len(primes) - 1 else primes[index:]
