''' 
Goldbach's Conjecture states that "Every even number greater than 4 is the sum of two odd prime numbers". 

Christian Goldbach composed this idea in 1742, after proposing his idea in a letter to Leonhard Euler, and it remains unproven to this day. To investigate this, I plan to formulate code that will check whether this conjecture holds for the first N even numbers (for a given N).

Firstly, I considered using code based on the sieve of Eratosthenes, which would take an integer N and returns a list of primes less than N. This would help generate the list from which an even number greater than 4 should be the sum of two of its elements.'''

def Eratosthenes(n):
    primes = list(range(2,n))
    for i in primes :
        j=2
        while i*j<=primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j = j+1
    return primes

'''Next, I would need to define a function to check every even number from 4 to a given N as to whether it complies with the conjecture. The code is as follows, where some lines have been annotated for explanation. '''

def Goldbach_check(N):
    n = 6
    primes = Eratosthenes(N) #creating a list of primes < N
    while n < N: #n is the even number being tested
        for i in primes: 
            for j in primes: 
                if j < i: # We only test if j >= i, to avoid checking the same pair of primes
                    continue
                if i + j == n: 
                    print(i,'+',j,'=',n)
                    break 
            if i + j == n: #This stops the function when it finds one solution
                           #Later, I will investigate how many different ways an even number can be represented as a sum of 2 primes
                break 
        n += 2

'''By running the code above for some N, python will print the sentence "i+j=n" for every n (an even number between 4 and N) with i,j as two prime numbers that form a solution. However, in some cases, there is more than one solution for i and j. We can see this by eliminating the following lines of code from the program above:
    if i+j==n:
        break
and leave the n+=2 as is. This means the loop will continue until it has found all pairs of solutions for i,j. Then, it will continue for each n. In order to compute this number of solutions, I want to create a similar function that will add the solutions to a list, and then add the number of solutions for each n to another list. I will then be able to produce a graph to plot the even numbers against the number of solutions for i,j'''

import matplotlib.pyplot as plt

def Goldbach_count(N):
    n = 6
    primes = Eratosthenes(N) 
    number_of_solutions=[]
    while n < N:
        solutions=[]
        for i in primes: 
            for j in primes: 
                if j < i: 
                    continue
                if i + j == n: 
                    #print(i,'+',j,'=',n)
                    solutions.append([i,j])
                    break 
        number_of_solutions.append(len(solutions))        
        n += 2
    print(number_of_solutions) 
    
'''After running this code (including lines 87 and 92), we can see that by entering "Goldbach_alternative(15)" in to the IPython console, we obtain the following output:
 2 + 2 = 4
 3 + 3 = 6
 3 + 5 = 8
 3 + 7 = 10
 5 + 5 = 10
 5 + 7 = 12
 3 + 11 = 14
 7 + 7 = 14
 [1, 1, 1, 2, 1, 2]
where the list at the bottom represents the number of solutions for primes i,j, where i+j=n, for each even number (starting from 4) up to n<15. Using this, we can extend the code to plot a graph of each even number against the number of i,j solutions.'''

    plt.plot(list(range(6,N,2)),number_of_solutions)
    plt.xlabel('Even number, n')
    plt.ylabel('Number of solutions for i+j=n')
    plt.title('Number of Ways to Write an Even Number as the Sum of Two Primes')
    
'''Now, entering the code "Goldbach_count(N)" will produce a graph that shows how many solutions exist for each even number from 4 to N to be represented as the sum of two primes. This does, in fact, support Goldbach's conjecture as entering large numbers of N (e.g. N=1000) produces a graph known as Goldbach's comet. For Goldbach's conjecture to be false, we should see a zero value somewhere to the right of the graph, for some large N. The graph is named as such for it's fascinating pattern for which the values for each n display themselves as "streaks", making it look someone similar to how we would picture a comet. 

///Lemoine's Conjecture///

In 1894, Émile Lemoine stated his own conjecture, that "Every odd number greater than 5 is the sum of a prime and the double of a prime. This is similar to, and also, stronger than, Goldbach's weak conjecture that states "Every odd number greater than 5 can be expressed as the sum of three primes" (where a prime may be used more than once in the same sum.) Algebraically, this can be represented as 2n + 1 = p + 2q always having a solution for some primes p and q, for n > 2.

We can write a program to investigate this as follows:'''

def Lemoine(N):
    x = 0
    y = 0
    result = 0
    if N % 2:
        prime = eratosthenes(N)
        while result != N:
            for i in range(len(prime)):
                x = prime[i]
                if result == N: 
                    break
                for j in range(len(prime)):
                    y = prime[j]
                    result = 2*x + y
                    if result == N: 
                        print('2*',x,'+',y,'=',N)
                        break

'''For example, after running the code, if we input "Lemoine(23)" in to the IPython console then we receive the output "2* 2 + 19 = 23" which shows that Lemoine's conjecture is true for the number 23. We can then test this for larger numbers of N, such as 9999, where Python calculates that 2*13+9973=9999. By observation, it appears that Python will present the solution involving the smallest possible value of x, for which 2*x+y=N. However, it is assumed that some numbers that more than one solution for this, as was apparent in Goldbach's conjecture.

///Disproving a False Conjecture///

Another conjecture that Goldbach proposed stated "Every odd composite number can be written as the sum of a prime and twice a square." However, this conjecture was found to be false, and so I want to produce a program that will find the smallest counterexample that disproves this.

We want to create a loop that checks whether a number is composite (i.e. not prime and greater than 3) the number is equal to the sum of a prime and twice a square. Firstly, we can write a function that checks if a number is prime, as follows:'''
                   
def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True    

'''Now, we want to create the while loop that checks each number for if it violates the conjecture.'''

from math import sqrt
N = 3
primes = [2] #an inital list of primes

while True:
    if is_prime(N):
        primes.append(N) #adds primes (non-composites) to a list
    else:
        for i in primes:
            if sqrt(((N-i)/2)) == int(sqrt(((N-i)/2))): 
                #this tests if N is equal
                #to the sum of a prime (i) and twice a square, by rearranging
                #the formula, for if it were true
                break
        else:
            print('The smallest counterexample for Conjecture 3 is', N) 
            # This line of code will first run for the smallest counterexample
            # which is what we want to find
            break
    N += 2
    
''' As a side note, my initial thoughts to investigate this conjecture involved creating a list consisting of odd composite numbers, less than N. I figured I would then be able to test whether a number in the list could be represented as a sum of a prime and the double of a square. The code I wrote for this is as follows:'''

def Odd_composite(N):
    mylist=list(range(2,N))
    for i in eratosthenes(N):
        mylist.remove(i)
        for j in mylist:
            if (j%2 == 0):
                mylist.remove(j)
    return mylist  

'''However, I decided that it would be more efficient to create a while loop, which would continue indefinitely until it found a counterexample. By testing if the given number in the loop was prime, this was an easy way to discard it as a counterexample, as opposed to trying to only test numbers in a list of composite numbers, when we could not initially determine how large we would need to set N.'''  
