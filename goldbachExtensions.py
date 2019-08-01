#C:\Users\Mike\AppData\Local\Programs\Python\Python37-32\python.exe C:\Users\Mike\Desktop\python\goldbachExtensions.py
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

primes = [-1,0,1] #we may include 1, 0, or some negatives of primes as additional 'primes' in order to get some smaller solutions
primeStart = len(primes) #the index of the first prime number, namely "2".
						 #This index is usually zero, but may increase if we include 1, 0, -1, -2, etc.

possPrime = 2 #integer to check for primality, starts at 2 and increases to maxPossPrime

#********EDIT HERE********
#This number roughly determines the upper limit of n, so for checking larger numbers, use a larger value here
maxPossPrime = 50 #count to this prime number candidate and then stop

while possPrime < maxPossPrime:
	
	divisor = 2 #we will divide possPrime by every plausible integer, not just primes.  This is to make the code cleaner
	#We could divide only by primes, but it's a tiny part of the runtime either way.
	
	highestDivisor=math.sqrt(possPrime) #we check only up to the square root of possPrime
	maybePrime = 1 #this is set to 1 unless and until we find a number that evenly divides possPrime
	
	while divisor <= highestDivisor:  #stop when the divisor gets high enough to be unneeded
		
		remainder=possPrime%divisor #check if there is no remainder
		if remainder == 0: 			#if there's no remainder,
			maybePrime = 0 			#then possPrime is not prime
			divisor = possPrime 	#and so, increase divisor to a relatively large number so that the loop will break
			
		divisor += 1
	
	if maybePrime == 1: 			#if it's still maybe a prime and we've checked 
		primes.append(possPrime)	#every case where it could fail out, it is prime
		
	possPrime += 1
	

#part two
#This second section picks two coefficients and builds a list of their factors

#*************EDIT HERE*************
#Edit this part of the code to pick which equation you want to solve for
#A and B must be relatively prime, or only trivial solutions will be found
A=7
B=2

#the following builds a list of prime factors of A and B
factors_AB = []
possFactorIndex=primeStart #sets our possible factor index to the index of the first prime (namely, 2).  Usually this index is simply zero.
while primes[possFactorIndex] <= A: #check all primes less than A
	
	if A%primes[possFactorIndex] == 0: #if this prime is a factor,
		
		factors_AB.append(primes[possFactorIndex]) #add it to the list of factors
	
	possFactorIndex += 1
	
possFactorIndex=primeStart #reset back to the index of 2.
while primes[possFactorIndex] <= B: #check all primes less than B

	if B%primes[possFactorIndex] == 0: #if this prime is a factor,
		
		factors_AB.append(primes[possFactorIndex]) #add it to the list of factors

	possFactorIndex += 1
#print(factors_AB)  #unhide this to double check that the factors are what you expected

#part three
#This third section has two halves
#The first half checks if possSolution is a solution to Ap+Bq
	#possSolution is either all evens or all odds
	#except for numbers not relatively prime to either A or B
#The second half checks whether the next possSolution is relatively prime to A or B,
	#and if it isn't relatively prime, that possSolution is not checked

#possSolution is our iterative variable to check which numbers have solutions.
#The earliest possible match that we will check is 3A + 3B.  Be careful trying for lower solutions, because the even or oddness might change.
possSolution=(3*A)+(3*B)

match = 0 #match is a variable that checks whether A (or B) is relatively prime to possSolution

while possSolution < primes[len(primes)-2]: #this loop finds solutions and can display them.  At the least it will declare if no solutions are found
											#The loop has confusing behavior if it reaches the very last prime, so we stop before then.
	
	pIndex = 0
	Ap = A*primes[pIndex]  #the 'left chunk' of Ap + Bq .......
	solutionFound = 0
	
	if match == 0:
		while Ap < A*primes[len(primes)-2]:
		
			qIndex = 0
			
			if A == B: #true in the base case of A = B = 1
				
				qIndex = pIndex #in the base case we want to skip counting the same solution twice, so jump qIndex up.
								#Don't jump qIndex up to pIndex in any other case.
			
			Bq = B*primes[qIndex] #...... the 'right chunk' of Ap + Bq
			
			while Bq <= B*primes[len(primes)-2]:
			
				#this checks for solutions of the form Ap + Bq (goldbachy solutions)
				if possSolution == Ap+Bq:
				
					solutionFound = 1   #frequently, more than one solution will be found, so this indicator may already be at 1
					#*********************************************COMMENT THIS LINE IN OR OUT*********************************************
					#hide the following line to stop the spamming of successful solutions
					print(str(possSolution) + " = (" + str(A) + " * " + str(primes[pIndex]) + ") + (" + str(B) + " * " + str(primes[qIndex]) + ")")
				
				#this checks for solutions of the form Ap - Bq (gaps between primes)
				#if possSolution == Ap-Bq:
				
					#solutionFound = 1
					#print(str(possSolution) + " = (" + str(A) + " * " + str(primes[pIndex]) + ") - (" + str(B) + " * " + str(primes[qIndex]) + ")")
				
				qIndex += 1
				Bq = B*primes[qIndex]
			
			pIndex += 1
			Ap = A*primes[pIndex]
		
		if solutionFound == 0:
			
			print(str(possSolution) + " has no match")
		
	possSolution += 2
	
	#we have a list of factors of A and B
	#we must check if possSolution now shares any factors with A or B (we want to exclude trivial exeptions)
	
	#the following builds a list of factors of possSolution
	q1=primeStart
	factors_possSolution = []
	while primes[q1] <= possSolution : #check all primes less than possSolution
	
		if possSolution%primes[q1] == 0: #if this prime is a factor,
		
			factors_possSolution.append(primes[q1]) #add it to the list of factors
	
		q1 += 1
	#print(factors_possSolution)	
	
	#now, we do a nested loop to check if there are any common factors between possSolution and A or B
	#if we have a match, we skip checking it up above
	match = 0
	i=0
	j=0
	while i < len(factors_AB):
		
		while j < len(factors_possSolution):
			
			if factors_AB[i] == factors_possSolution[j]:
			
				match = 1	#turn this to 0 to see all the trivial exceptions
			
			j += 1
			
		j=0
			
		i += 1
	
#end