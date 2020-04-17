'''
<Maximally_Periodic_Reciprocals mneumonic="Sophie German Prime" finished=true/> 
<notes>
    Sophie Germain primes may be used in the generation of pseudo-random numbers.
    The decimal expansion of 1/q will produce a stream of q − 1 pseudo-random digits,
    if q is the safe prime of a Sophie Germain prime p, with p congruent to 3, 9, or 11 (mod 20).
    Thus "suitable" prime numbers q are 7, 23, 47, 59, 167, 179, etc. (OEIS: A000353) 
    (corresponding to p =  3, 11, 23, 29, 83, 89, etc.) (OEIS: A000355). 
    The result is a stream of length q − 1 digits (including leading zeros). 
    So, for example, using q = 23 generates the pseudo-random digits 0, 4, 3, 4, 7, 8, 2, 6, 0, 8, 6, 9, 5, 6, 5, 2, 1, 7, 3, 9, 1, 3.
    Note that these digits are not appropriate for cryptographic purposes, as the value of each can be derived from its predecessor in 
    the digit-stream. 
    
    This only works when you input a prime number that
    a. is a sophie prime.(if p is prime and 2*p + 1 is also a prime, p is a sophie prime)
    b. listlength >= safeprime
    
    --and--
    
    listlength > decprec
    
    Note that this will not accurately return the list length requested. It will return listlength - 2
    
    If p is a Sophie Germain prime greater than 3, then p must be congruent to 2 mod 3. 
    For, if not, it would be congruent to 1 mod 3 and 2p + 1 would be congruent to 3 mod 3,
    impossible for a prime number....
    ... We are taking a brute force approach and just checking if the alleged safe prime is indeed prime, instead of 
    checking modulo restrictions to short circuit the operation. This is less efficient, but it is OK for now to brute force it.
    
</notes>

'''
def Maximally_Periodic_Reciprocals(p, listlength, decprec=100):
    # In number theory, a prime number p is a Sophie Germain prime if 2p + 1 is also prime.
    
    #make whole
    p = int(p)
    
    #prime check
    if(not IsPrime(p)):
        print("p is not prime")
        return
    
    #sophie check 
    safeprime = 2 * p + 1
    if(not IsPrime(safeprime)):
        print("p is prime, but isn't a sophie prime.")
        return
    
    #listlength check
    #1/q will produce q-1 pseudo random digits.
    if(listlength >= safeprime):
        print("p is a sophie prime, but your list length is greater than or equal to the # of digits of p's safe prime (q): ", 
              str(safeprime),
              "\n... Because 1/q will produce q-1 pseudo random digits.")
        return
    
    #decprec check
    if(listlength > decprec):
        print("p is a sophie prime, but you are requesting a list longer than specified decimal precision.")
        return 
    
    print("You have passed prime check, sophie check, safeprime_listlength check , and decprec_listlength check.")
    
    # p has been confirmed to be a sophie prime. var safeprime is now p's safe prime.
    q = safeprime
    
    # if q is the safe prime of a Sophie Germain prime p, 1/q will produce q-1 pseudo random digits.
    getcontext().prec = decprec
    LotsOfPseudos = Decimal(1) / Decimal(q)
    
    #print("length",len(str(LotsOfPseudos)))
    
    numlist = []
    
    #note that this will not accurately return the list length requested. It will return list length - 2
    for i in range(listlength):
        if(i is not 0 and i is not 1):#str(LotsOfPseudos)[i] is not '.'):
            numlist.append(str(LotsOfPseudos)[i])
        
    return numlist
