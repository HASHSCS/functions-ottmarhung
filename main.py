def square(n):

    if n % 1 == 0:
        print("int")
        print(n*n)
        return(n*n)
    else:
        print("float")
        print(n*n)
        return(n*n)
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    
    Implement your solution here
    """
    pass  # Implement your solution here
square(1)
print("******************")


def reverse_string(s):
    b = 0
    c = ""
    for i in range(len(s)-1,-1,-1):
        
        c+=s[i]
        b += 1
    
    print(c)
    return(c)
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    pass  # Implement your solution here
reverse_string("string")
print("******************")
def is_prime(n):
    b = 0
    for i in range(n,0,-1):
        a = n%i
        if a ==0:
            b += 1
            print(b)
    if b == 2:
        print("prime")
        return(True)
    else:
        print("not prime")
        return(False)
    """
    This function takes a number as input and returns True if the number is prime, otherwise False.
    :param n: int
    :return: bool, True if the number is prime, otherwise False
    """
    pass  # Implement your solution here
is_prime(2)
print("******************")
def factorial(n):
    a = n
    for i in range(n,1,-1):
        a*=(i-1)
    if a== 0:
        print(1)
        return(1)
    print(a)
    return(a)    
    """
    This function takes a number as input and returns its factorial.
    :param n: int
    :return: int, the factorial of the input number
    """
  
    pass  # Implement your solution here
factorial(3)
print("******************")
def find_maximum(lst):
    a = lst[0]
    for i in range(0,len(lst)-1):
        if a<=lst[i+1]:
            a = lst[i+1]
            print(a)
        
    print(a)
    return(a)
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    pass  # Implement your solution here
find_maximum([1,2,3,4,5])
print("**********************")
def odd_or_even(n):
    if n%2 == 0:
        print("Even")
        return("Even")
    elif n %2 ==1:
        print("Odd")
        return("Odd")
    else:
        ("error") 
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    pass  # Implement your solution here
odd_or_even(2)
print("******************")
import math
def is_palindrome(s):
    if len(s)%2 == 0:
        a = len(s)-1

    else:
        a = len(s)-len(s)%1 -1
    b = a/2
    b=math.floor(b)
    c = 0
    d = a

    for i in range(0,b):
        if s[i] == s[d]:
            c+=1
            d-=1

    if c == b or s =="":
        print("palindrome")
        return(True)
    else:
        print("notpalindrome")
        return(False)
    

    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    pass  # Implement your solution here
is_palindrome("")
print("******************")

def prime(pi,pb,pc,pg):
  
    if isinstance(pb,int)==True:
            while pi <= pb and pb>0 :
                if pb%pi == 0:
                    pc = pb/pi
                    pg.append(pc)
                    pi +=1
                else:
                    pi+=1 

    
    
      
def find_gcd(a,b):   
    ii = 1
    ab = a
    c=0
    ag = []
        
    iii = 1
    bb = b
    cb =0
    bg = []
    wtc = 0
    prime(ii,ab,c,ag)
    prime(iii,bb,cb,bg)    
    d = 0
    if len(bg) >= len(ag):
        wtc = len(bg)
        wtl = len(ag)
        wtg = bg
        wtgl = ag
    else:
        wtc = len(ag)
        wtl = len(bg)
        wtg = ag
        wtgl = bg
    s = wtl-1
    mmm = 0
    for i in range(wtc-1,-1,-1):
        for s in range(wtl-1,-1,-1):
            if wtg[i] == wtgl[s]:
                mmm = wtg[i]
    print(mmm)
    return(mmm)
      
"""
    This function takes two positive integers `a` and `b` and returns their greatest common divisor (GCD).
    
    :param a: int
    :param b: int
    :return: int, the greatest common divisor of `a` and `b`.
    """
pass  # Implement your solution here
find_gcd(100,144)
