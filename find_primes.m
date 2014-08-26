format long
dlmwrite('primes.txt', setxor(primes(10000000),primes(500000)), 'precision', '%.0f');
