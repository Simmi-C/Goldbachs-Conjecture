# Goldbachs Conjecture
A study of Goldbach's conjecture, the sieve of Eratosthenes and Lemoine's conjecture

Goldbach's Conjecture states that "Every even number greater than 4 is the sum of two odd prime numbers". Christian Goldbach composed this idea in 1742, after proposing his idea in a letter to Leonhard Euler, and it remains unproven to this day. To investigate this, I plan to formulate code that will check whether this conjecture holds for the first N even numbers (for a given N).

Firstly, I considered using code based on the sieve of Eratosthenes, which would take an integer N and returns a list of primes less than N. This would help generate the list from which an even number greater than 4 should be the sum of two of its elements. 

def Eratosthenes(n):
    primes = list(range(2,n))
    for i in primes :
        j=2
        while i*j<=primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j = j+1
    return primes
    
 
