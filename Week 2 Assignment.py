'''
Write three Python functions as specified below. Paste the text for all three functions together into the submission window.
You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to
check for malformed inputs.
For each function, there are some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases and report a score on 100. There are 15 private 
testcases in all, each with equal weightage.
Ignore warnings about "Presentation errors".
Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

  >>> intreverse(783)
  387
  >>> intreverse(242789)
  987242
  >>> intreverse(3)
  3
Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, 
every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols
that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.

 
  >>> matched("zb%78")
  True
  >>> matched("(7)(a")
  False
  >>> matched("a)*(?")
  False
  >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
  True
Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

  >>> sumprimes([3,3,1,13])
  19
  >>> sumprimes([2,4,6,9,11])
  13
  >>> sumprimes([-3,1,6])
  0
Sample Test Cases
Input	Output
Test Case 1	
intreverse(368)
863
Test Case 2	
intreverse(798798)
897897
Test Case 3	
intreverse(7)
7
Test Case 4	
matched("(7)(a")
False
Test Case 5	
matched("a)*(?")
False
Test Case 6	
matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
Test Case 7	
sumprimes([17,51,29,39])
46
Test Case 8	
sumprimes([-3,-5,3,5])
8
Test Case 9	
sumprimes([4,6,15,27])
0
Test Case 10	
intreverse(31511)
11513
Test Case 11	
intreverse(4)
4
Test Case 12	
intreverse(15135324234235)
53243242353151
Test Case 13	
matched("a3qw3;4w3(aasdgsd)((agadsgdsgag)agaga)")
True
Test Case 14	
matched("(ag(Gaga(agag)Gaga)GG)a)33)cc(")
False
Test Case 15	
matched("(adsgdsg(agaga)a")
False
Test Case 16	
matched("15ababa.agaga[][[[")
True
Test Case 17	
sumprimes([101,93,97,44])
198
Test Case 18	
sumprimes([1001,393,743,59])
802
Test Case 19	
sumprimes([11,11,11,13,11,-11])
57
'''
#----------My solution---------------------
def intreverse(n):
    temp=0
    while (n !=0):
        temp = temp*10 + n%10
        n = int (n/10)
    return (temp)
  
  
#Q2
def matched(s):
    num=0
    for i in s:
        if i=='(' :
            num+=1
        elif  i==')' and num > 0 :
            num-=1
    if ( num==0 ):
        return (True)
    else:
        return (False)

def isprime(n):
    if n<=1:
        return (False)
    for i in range( 2, int( n**0.5) +1 ):
        if n%i==0:
            return (False)
    return (True)
def sumprimes(l):
    sum=0
    for i in l:
        if isprime(i):
            sum+=i
    return (sum)


#----------Instructure's solution---------------------
def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)

def matched(s):
  nested = 0
  for i in range(0,len(s)):
    if s[i] == "(":
       nested = nested+1
    elif s[i] == ")":
       nested = nested-1
       if nested < 0:
          return(False)    
  return(nested == 0)

def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)

def isprime(n):
  return(factors(n) == [1,n])


def sumprimes(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum+l[i]
  return(sum)
