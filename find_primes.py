from math import ceil, sqrt

def main():
    """
    Gets all primes between 500,000 and 10,000,000
    Written for Codecademy challenge
    """
    findPrimes(500001, 10000000, 'primes.txt')

def findPrimes(lo, hi, filename):
    """
    Gets all the primes between lo and hi
    """
    if not isinstance(lo, (int, long)) and not isinstance(hi, (int, long)):
        raise AssertionError('Lower and upper bounds must be integers')
    if lo < 0:
        raise AssertionError('Lower bound must be a positive number')
    if hi <= lo:
        raise AssertionError('Upper bound must be greater than the lower bound')

    f = open(filename, 'a')
    # Brute force search when the inputs are small, otherwise optimizations
    # are needed
    if lo < 100000 and hi - lo < 1000000:
        for x in xrange(2, hi):
            if isPrime(x, 2):
                f.write(str(x)+',\n')
    else:
        LITTLE_PRIMES = []
        # First, get a list of all primes < 1000
        # This will be used as an optimization later on.
        for x in xrange(3, 1000):
            # Optimization: We're going to skip even numbers.
            # We'll check for it later.
            if x & 1:
                pass
            else:
                continue
            if isPrime(x, 3):
                LITTLE_PRIMES.append(x)

        # Write out all primes < 1000 first, if lo < 1000
        if lo < 1000:
            for i in xrange(lo, 1000):
                if isPrime(i, 2):
                    f.write(str(i)+',\n')

        # Check if the number is prime. Loop between lo and hi
        for num in xrange(max(lo, 1000), hi):
            b = False

            # Optimization: Even numbers are non-prime
            if num & 1:
                pass
            else:
                continue

            # Optimization: If the number is divisible by any of the first
            # primes < 1000, then it is non-prime
            for p in LITTLE_PRIMES:
                if num % p == 0:
                    b = True
                    break
            if b:
                continue
            # Start at 1000 since we've already checked all the primes < 1000
            if isPrime(num, 1000):
                f.write(str(num)+',')
    f.close()

def isPrime(num, start):
    """
    Brute-force division to check if num is prime
    start tells what number to begin checking at, assuming
    that you've already checked that all factors < start
    don't divide num.
    """
    # Optimization: We only need to do trial division up until sqrt(num)+1
    for x in xrange(start, int(ceil(sqrt(num))+1)):
        if num % x == 0:
            return False
    
    return True

if __name__ == '__main__':
    main()
