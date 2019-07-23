#C:\Users\Mike\AppData\Local\Programs\Python\Python37-32\python.exe C:\Users\Mike\Desktop\python\goldbach1.py
import math

#The Goldbach Conjecture asserts that every even number above 3 is the sum of two primes, or
#p + q = 2n always has a solution.

#An evident feature of these solutions is that as n grows larger, smaller primes may be safely ignored.
#For example, 2 is used to find a solution for 4, but above that is unnecessary, and 3 may be dropped when finding solutions above 8 (conjectured).

#part one
#This generates a list of prime numbers

primes = [] #we may include 1 as a 'prime' in order to get some smaller solutions
primeStart = len(primes) #start at 1 if 1 is included, and 0 if it is not

c=5 #this is our lower limit for primes
max = 224 #this is (roughly) our upper limit for primes

while c < max:
	
	d=2
	e=math.sqrt(c)
	maybePrime = 1
	
	while d <= e:
		
		f=c%d #check if there is no remainder
		if f == 0:
			maybePrime = 0
			
		d += 1
	
	if maybePrime == 1:
		primes.append(c)
		
	c += 1

#part two
#This checks for solutions to p + q = 2n with p,q constrained by our arbitrary min and max.
#With a higher minimum, small solutions will be less likely to be possible, 
#while larger solutions should remain possible.

matches = []
x=2

while x < primes[len(primes)-2]:
	
	matchFound = 0
	
	p=0
	y = primes[p]
	
	while y < x:
		
		q=p
		z = primes[q]
		
		w=x-y
		while z <= w:
			
			if x == y+z:
			
				matchFound = 1
				print(str(x) + " = " + str(y) + " + " + str(z))
				
			q += 1
			z = primes[q]
			
		p += 1
		y = primes[p]
		
	if matchFound == 0:
			
		print(str(x) + " has no match")
				
	x += 2
	