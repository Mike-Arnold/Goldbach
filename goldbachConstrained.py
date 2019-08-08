#C:\Users\Mike\AppData\Local\Programs\Python\Python37-32\python.exe C:\Users\Mike\Desktop\python\goldbachConstrained.py
import math

#The Goldbach Conjecture asserts that every even number above 3 is the sum of two primes, or
#p + q = 2n always has a solution.

#An evident feature of these solutions is that as n grows larger, smaller primes may be safely ignored.
#For example, 2 is used to find a solution for 4, but above that is unnecessary, and 3 may be dropped when finding solutions above 8 (conjectured).

#part one
#This generates a list of prime numbers

primes = [1] #we may include 1 as an additional 'prime' in order to get some smaller solutions
primeStart = len(primes) #the index of the first prime number, namely "2".
						 #This index is usually zero, but may increase if we include 1, or negative primes

possPrime = 2 #integer to check for primality, starts at 2 and increases to maxPossPrime

#********EDIT HERE********
#This number roughly determines the upper limit of n, so for checking larger numbers, use a larger value here
maxPossPrime = 50 #count to this prime number candidate and then stop

while possPrime < maxPossPrime:
	
	divisor = 2 #we will divide possPrime by every plausible integer, not just primes.  This is to make the code cleaner
	#We could divide only by primes, but it's a tiny part of the runtime either way.
	
	highestDivisor=math.sqrt(possPrime) #we check only up to the square root of possPrime
	maybePrime = 1 #this is set to 1 (TRUE) unless and until we find a number that evenly divides possPrime
	
	while divisor <= highestDivisor:  #stop when the divisor gets high enough to be unneeded
		
		remainder=possPrime%divisor #check if there is no remainder
		if remainder == 0: 			#if there's no remainder,
			maybePrime = 0 			#then possPrime is not prime (zero is FALSE)
			break 	
			
		divisor += 1
	
	if maybePrime == 1: 			#if it's still maybe a prime and we've checked 
		primes.append(possPrime)	#every case where it could fail out, it is prime
		
	possPrime += 1
	
print("Primes: " + str(len(primes)))

#part two
#This checks for solutions to p + q = 2n with p,q constrained by our arbitrary min and max.
#With a higher minimum, small solutions will be less likely to be possible, 
#while larger solutions will often remain possible, despite the constraint.

possSolution=2  #this is the '2n' in 'p + q = 2n'.  It will be incremented by 2.  
				#We want to start at 2 in order to check the lowest values, and find the lowest value after which there are always solutions.
pretendLowestPrimeIndex = 0  #we constrain ourselves by ignoring some of the first few primes.  Set this to zero for no constraint.

while possSolution < primes[len(primes)-2]:
	
	matchFound = 0  #set to FALSE ___ If we never get a match it'll stay FALSE
	
	pIndex=pretendLowestPrimeIndex  #we'll use primes[pIndex] for p, and start it where our constraint tells us to
	
	while primes[pIndex] < possSolution:  #p can't be larger than 2n
		
		qIndex=pIndex #and we use primes[qIndex] for q.  Without loss of generality, we'll have p less than q (or equal)
		
		while primes[pIndex] + primes[qIndex] <= possSolution: #p + q can't be larger than 2n
			
			if possSolution == primes[pIndex]+primes[qIndex]:  #that's 2n = p + q !
			
				matchFound = 1  #set this to TRUE, so omit the 'no match' message for this 2n
				print(str(possSolution) + " = " + str(primes[pIndex]) + " + " + str(primes[qIndex]))  #displays the solution in detail
				
			qIndex += 1
			
		pIndex += 1
		
	if matchFound == 0:  #this is if we never got a match and want to be alerted
			
		print(str(possSolution) + " has no match")
				
	possSolution += 2  #2n + 2 ___ We're only checking even solutions
	