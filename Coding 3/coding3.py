# -*- coding: utf-8 -*-
"""coding3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H8J2a_vh9xjciXave_YjXbCLPxcNQVl2
"""

# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 3

# YOUR NAME(s): Sophie Johnson, Anya Devgan
# YOUR UNI(s): smj2173, ad3706

import math
import random

'''
Returns the GCD of two integers using Euclid's algorithm. Also prints out the
intermediate steps for Euclid's Algorithm on num1 and num2.

Parameters:
num1 (int): First number for the GCD
num2 (int): Second number for the GCD

Returns:
int: GCD of num1 and num2
'''
def euclid(num1, num2):
    print('GCD({},{})'.format(num1, num2), end = ' ')

    while (num1 != 0 and num2 != 0):
      remainder = num1 % num2
      num1 = num2
      num2 = remainder
      print('= GCD({},{})'.format(num1,num2), end = ' ')
    
    if (num1 == 0 and num2 == 0):
      print(' none ')
      return None #GCD does not exist
    elif (num1 == 0):
      print('= GCD({},{})'.format(num2,num1), end = ' ')
      print('= {}'.format(num2))
      return num2
    else: #num2 == 0
      print('= {}'.format(num1))
      return num1
  

'''
Returns a list of prime numbers up to (and including) a certain input integer, n.

Parameters:
n (int): The target number to generate primes up to.

Returns:
list: List of all prime numbers <= n.
'''
def prime_gen(n):
    primes = []
    boolean_check = [True for elm in range(n+1)]
    boolean_check[0] = False #0 is not a prime number
    boolean_check[1] = False #1 is not a prime number

    p = 2
    while(p*p < n):
      if(boolean_check[p] == True):
        for x in range (p*p, n+1, p):
          boolean_check[x] = False
      p = p + 1

    for elem in range(n+1):
      if boolean_check[elem] == True:
        primes.append(elem)
    
    return primes # your list of prime numbers

'''
Returns a boolean value (True or False) depending on whether the input n is prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''
def prime_check_trial(n):
    if n == 0 or n == 1:
      prime = False
      return prime
    for x in range(2, (int)(math.sqrt(n))+1):
      if n % x == 0:
        prime = False
        return prime
    prime = True
    return prime # boolean True or False depending on prime or not

'''
Returns a boolean value (True or False) depending on whether the input n is prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''
def prime_check_sieve(n):
    if n <= 1:
      prime = False
      return prime
    for x in range (2,n):
      if(n % x == 0):
        prime = False
        return prime
    prime = True
    return prime # boolean True or False depending on prime or not

'''
Returns a list of two prime integers that sum up to n.

Parameters:
n (int): The target even integer to check Goldbach's Conjecture for.

Returns:
list: A list of length 2 containing 2 ints that sum up to n.
'''
def check_goldbach(n):
    primes = []
    if n == 2:
      primes = None
    else:
      primes = prime_gen(n)
      for p in primes:
        if(n-p) in primes:
          primes = [p,(n-p)]
    return primes # two prime numbers that sum up to n

### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 2: Prime Numbers!")
    print("#######################################")
    print()

    print("---------------------------------------")
    print("PART A: Euclid's Algorithm")
    print("---------------------------------------")
    euclid_test_1 = [252, 105]
    print("Test Case 1: GCD of", euclid_test_1[0], "and", euclid_test_1[1])
    print("Test Case 1 Steps: ")
    student_ans = euclid(euclid_test_1[0], euclid_test_1[1])
    print("Test Case 1 (Your Answer):", student_ans)
    print("Test Case 1 (Correct Answer):", 21)
    print("Test Case 1:", ("# PASSED! #" if student_ans == 21  else "# INCORRECT #"))
    print()
    euclid_test_2 = [1071, 462]
    print("Test Case 2: GCD of", euclid_test_2[0], "and", euclid_test_2[1])
    print("Test Case 2 Steps: ")
    student_ans = euclid(euclid_test_2[0], euclid_test_2[1])
    print("Test Case 2 (Your Answer):", student_ans)
    print("Test Case 2 (Correct Answer):", 21)
    print("Test Case 2:", ("# PASSED! #" if student_ans == 21  else "# INCORRECT #"))
    print()
    euclid_test_3 = [85523, 3212]
    print("Test Case 3: GCD of", euclid_test_3[0], "and", euclid_test_3[1])
    print("Test Case 3 Steps: ")
    student_ans = euclid(euclid_test_3[0], euclid_test_3[1])
    print("Test Case 3 (Your Answer):", student_ans)
    print("Test Case 3 (Correct Answer):", 1)
    print("Test Case 3:", ("# PASSED! #" if student_ans == 1  else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART B: Prime Number Generation")
    print("---------------------------------------")
    prime_gen_test_1 = 42
    prime_gen_test_1_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    print("Test Case 1: Prime Numbers Up To:", prime_gen_test_1)
    print("Test Case 1 (Your Answer):", prime_gen(prime_gen_test_1))
    print("Test Case 1 (Correct Answer):", prime_gen_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if prime_gen(prime_gen_test_1) == prime_gen_test_1_ans  else "# INCORRECT #"))
    print()
    prime_gen_test_2 = 314
    prime_gen_test_2_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
    131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313]
    print("Test Case 2: Prime Numbers Up To:", prime_gen_test_2)
    print("Test Case 2 (Your Answer):", prime_gen(prime_gen_test_2))
    print("Test Case 2 (Correct Answer):", prime_gen_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if prime_gen(prime_gen_test_2) == prime_gen_test_2_ans  else "# INCORRECT #"))
    print()
    prime_gen_test_3 = 884
    prime_gen_test_3_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
    199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
    491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883]
    print("Test Case 3: Prime Numbers Up To:", prime_gen_test_3)
    print("Test Case 3 (Your Answer):", prime_gen(prime_gen_test_3))
    print("Test Case 3 (Correct Answer):", prime_gen_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if prime_gen(prime_gen_test_3) == prime_gen_test_3_ans  else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART C: Primality Testing")
    print("---------------------------------------")
    primality_test_1 = 8
    primality_test_1_ans = False
    print("Test Case 1: Check Primality For:", primality_test_1)
    print("Test Case 1 (Your Trial Division Answer):", prime_check_trial(primality_test_1))
    print("Test Case 1 (Your Sieve Answer):", prime_check_sieve(primality_test_1))
    print("Test Case 1 (Correct Answer):", primality_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if prime_check_trial(primality_test_1) == prime_check_sieve(primality_test_1) == primality_test_1_ans else "# INCORRECT #"))
    print()
    primality_test_2 = 482
    primality_test_2_ans = False
    print("Test Case 2: Check Primality For:", primality_test_2)
    print("Test Case 2 (Your Trial Division Answer):", prime_check_trial(primality_test_2))
    print("Test Case 2 (Your Sieve Answer):", prime_check_sieve(primality_test_2))
    print("Test Case 2 (Correct Answer):", primality_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if prime_check_trial(primality_test_2) == prime_check_sieve(primality_test_2) == primality_test_2_ans else "# INCORRECT #"))
    print()
    primality_test_3 = 853
    primality_test_3_ans = True
    print("Test Case 3: Check Primality For:", primality_test_3)
    print("Test Case 3 (Your Trial Division Answer):", prime_check_trial(primality_test_3))
    print("Test Case 3 (Your Sieve Answer):", prime_check_sieve(primality_test_3))
    print("Test Case 3 (Correct Answer):", primality_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if prime_check_trial(primality_test_3) == prime_check_sieve(primality_test_3) == primality_test_3_ans else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART D: Goldbach's Conjecture")
    print("---------------------------------------")
    goldbach_test_1 = 8
    goldbach_test_1_ans = [3, 5]
    student_ans = check_goldbach(goldbach_test_1)
    print("Test Case 1: 2 Primes For:", goldbach_test_1)
    print("Test Case 1 (Your Answer):", check_goldbach(goldbach_test_1))
    print("Test Case 1 (A Correct Answer):", goldbach_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_1  else "# INCORRECT #"))
    print()
    goldbach_test_2 = 482
    goldbach_test_2_ans = [3, 479]
    student_ans = check_goldbach(goldbach_test_2)
    print("Test Case 2: 2 Primes For:", goldbach_test_2)
    print("Test Case 2 (Your Answer):", check_goldbach(goldbach_test_2))
    print("Test Case 2 (A Correct Answer):", goldbach_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_2  else "# INCORRECT #"))
    print()
    goldbach_test_3 = 1152
    goldbach_test_3_ans = [23, 1129]
    student_ans = check_goldbach(goldbach_test_3)
    print("Test Case 3: 2 Primes For:", goldbach_test_3)
    print("Test Case 3 (Your Answer):", check_goldbach(goldbach_test_3))
    print("Test Case 3 (A Correct Answer):", goldbach_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_3  else "# INCORRECT #"))
    print("---------------------------------------")