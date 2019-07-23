import math

#The Goldbach Conjecture is an unproven statement that any even number is the sum of two primes, 
#or that for any n, you can find p and q to satisfy p + q = 2n.

#A natural extension has been conjectured for 2p + q = 2n + 1 (every odd number above 6 is a prime plus twice a prime)

#One might want to try 3p + q = 2n, but an infinite number of exceptions exist (2,4,6,18,24,30,36,etc...)
#The first of these (2,4,6) can be ignored because they are small.
#The rest are all multiples of 3, which are trivially impossible.
#Exceptions other than these two types have not been found.

#So, a general conjecture may be made which always demands solutions of the form Ap + Bq = n, 
#n is either odd or even and A,B,n are all relatively prime, and n is sufficiently large.
#A formula for when n is sufficiently large is unknown.


#This script finds solutions to Ap + Bq = n by brute force.
#Data suggest that this conjecture may be true, but a proof for any A,B remains undiscovered.

#part one
#This first section generates a list of prime numbers

primes = [] #we may include 1 as a 'prime' in order to get some smaller solutions
primeStart = len(primes) #start at 1 if 1 is included, and 0 if it is not

c=2 #first number to check for primality
max = 1000 #count to this prime number candidate and then stop

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
#This second section picks two coefficients and builds a list of their factors

#A and B must be relatively prime, or only trivial solutions will be found
A=5
B=2

#the following builds a list of prime factors of A and B
factors_AB = []
p1=primeStart
while primes[p1] <= A: #check all primes less than A
	
	if A%primes[p1] == 0: #if this prime is a factor,
		
		factors_AB.append(primes[p1]) #add it to the list of factors
	
	p1 += 1
	
p1=primeStart
while primes[p1] <= B: #check all primes less than B

	if B%primes[p1] == 0: #if this prime is a factor,
		
		factors_AB.append(primes[p1]) #add it to the list of factors

	p1 += 1
#print(factors_AB)

#part three
#This third section has two parts
#The first part checks if x is a solution to Ap+Bq
	#x is either all evens or all odds
	#except for numbers not relatively prime to either A or B
#The second part checks whether the next x is relatively prime to A or B,
	#and skips looking for a match if it shares any factors

#x is our iterative variable to check which numbers (either evens or odds) have solutions
#earliest possible match is 3A + 3B
x=(3*A)+(3*B)

match = 0 #match is a variable that checks whether A is relatively prime to x

while x < primes[len(primes)-2]: #we will check if x is equal to Ap +/- Bq

	p=0
	y = A*primes[p]
	solutionFound = 0
	
	if match == 0:
		while y < A*primes[len(primes)-2]:
		
			q=0
			
			if A == B:
				
				q = p #in the base case we want to skip counting the same solution twice
			
			z = B*primes[q]
			
			w=x-y
			while z <= B*primes[len(primes)-2]:
			
				#this checks for solutions of the form Ap + Bq (goldbachy solutions)
				if x == y+z:
				
					solutionFound = 1
					#hide the following line to stop the spamming of successful solutions
					#print(str(x) + " = (" + str(A) + " * " + str(primes[p]) + ") + (" + str(B) + " * " + str(primes[q]) + ")")
				
				#this checks for solutions of the form Ap - Bq (gaps between primes)
				#if x == y-z:
				
					#solutionFound = 1
					#print(str(x) + " = (" + str(A) + " * " + str(primes[p]) + ") - (" + str(B) + " * " + str(primes[q]) + ")")
				
				q += 1
				z = B*primes[q]
			
			p += 1
			y = A*primes[p]
		
		if solutionFound == 0:
			
			print(str(x) + " has no match")
		
	x += 2
	
	#we have a list of factors of A and B
	#we must check if x now shares any factors with A or B
		#numbers x which share any factors with A or B will create trivial exceptions in almost all cases
	
	#so let's build a list of factors of x
	
	#the following builds a list of factors of x
	q1=primeStart
	factors_x = []
	while primes[q1] <= x : #check all primes less than x
	
		if x%primes[q1] == 0: #if this prime is a factor,
		
			factors_x.append(primes[q1]) #add it to the list of factors
	
		q1 += 1
	#print(factors_x)	
	
	#now, we do a nested loop to check if there are any matches
	#if we have a match, we skip checking it up above
	match = 0
	i=0
	j=0
	while i < len(factors_AB):
		
		while j < len(factors_x):
			
			if factors_AB[i] == factors_x[j]:
			
				match = 1	#turn this to zero to turn off filtering of numbers that aren't relatively prime
			
			j += 1
			
		j=0
			
		i += 1
	
#end
