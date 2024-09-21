def oddOreven(n):
    if n%2 == 0:
        return True 
    return False 
    
def isPrime(n):
    if n<=1:
        return False
    for i in range(2, n//2 + 1):
        if n%i == 0:
            return False 
    return True 
    
def reverse(n):
    res = 0 
    while(n>0):
        rem = n % 10
        res = (res * 10) + rem
        n = n//10 
        
    return res 
    
def sumOfNumbers(n):
    add = 0 
    while(n>0):
        rem = n % 10 
        add+=rem 
        n = n//10
    return add 
    
def swapping(a,b):
    print("Before swapping: ", a, b)
    a = b - a 
    b = b - a 
    a = a + b 
    print("After swapping: ", a, b)
    
def isPalindrome(n):
    num = n 
    if(reverse(n) == num):
        return True 
    return False 
    
def findLargest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
        
def power(x,y):
    if y == 0:
        return 1 
    elif y == 1:
        return x 
    else:
        return x * power(x,y-1)
        
def sqrt(n):
    if n<=1:
        return n 
    res = 1 
    i = 1 
    while(res < n):
        i+=1 
        res = i * i 
    return i 
    
def average(a,b,c):
    add = a + b + c 
    avg = add//3 
    return avg 
    
def factorial(n):
    if n== 0:
        return 0
    f = 1 
    for i in range(1,n+1):
        f *= i 
    return f 
    
def permutation(n,r):
    permu = factorial(n)//factorial(n-r)
    return permu 
    
def combination(n,r):
    com = factorial(n)//(factorial(n-r) * factorial(r))
    return com 
    
def simpleInterest(P,R,T):
    SI = (P*R*T)/100 
    print("SI = ", SI)
    
def compoundInterest(P,R,T):
    amount = P * power(((1+R)/100), T)
    CI = P - amount 
    print("CI = ", round(CI,2))
    
def percentage(n,p):
    per = (n * p)/100 
    print(p, "Percentage of", n, "=", per)
    
def countofDigits(n):
    count = 0 
    while (n>0):
        n = n//10 
        count+=1 
    return count 
    
def isAmstrong(x):
    n = countofDigits(x)
    temp = x 
    add = 0 
    while(temp!=0):
       rem = temp % 10
       add += power(rem, n)
       temp = temp//10 
    if(add == x):
        return True 
    else:
        return False 
        
def fibonacci(n):
    n1 = 0 
    n2 = 1 
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1,n2 = n2,n3 
    print()
    
def gcd(x,y):
    res = min(x,y)
    while(res):
        if x%res == 0 and y%res == 0:
            break 
        res-=1 
    return res 
    
def lcm(x,y):
    res = (x * y)//gcd(x,y)
    return res 
    
def main():
    n = 64
    num = 23932
    a= 60
    b = 3 
    #odd or even
    if(oddOreven(n)):
        print(n, "is even number")
    else:
        print(n, "is odd number")
    
    #prime or not 
    if(isPrime(n)):
        print(n, "is prime number")
    else:
        print(n, "is not prime number")
        
    #Reverse number
    print("Reverse of", num, "=" ,reverse(num))
    
    #count number of digits 
    print("Number of digits in", num, "=", countofDigits(num))
    
    #sum of Numbers
    print("Sum of numbers in", num, "=", sumOfNumbers(num))
    
    #Palindrome or not 
    if(isPalindrome(num)):
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")
        
    #find square root of number 
    print("Square root of", n, "=", sqrt(n))
    
    #find Largest of 3 numbers 
    print("Largest of 3 numbers is", findLargest(n,a,b))
    
    #find power of number 
    print(a, "^", b, "=", power(a,b))
    
    #Swapping numbers 
    swapping(a,b)
    
    #Find average of 3 numbers 
    print("Average =", average(n,a,b))
    
    #find factorial 
    print("Factorial of", b, "=", factorial(b))
    
    #Simple Interest and compoundInterest
    simpleInterest(1000,20,5)
    compoundInterest(1000,20,5)
    
    #Permutation and combination
    print("5P3 =", permutation(5,3))
    print("5C3 =", combination(5,3))
    
    #Percentage 
    percentage(a,b)
    
    #Amstrong or not
    N = 513
    if(isAmstrong(N)):
        print(N, "is an Amstrong Number")
    else:
        print(N, "is not an Amstrong Number")
        
    #fibonacci series 
    digits = 10
    print("Fibonacci Series:", end ="")
    fibonacci(digits)
    
    #gcd or hcf of number 
    x = 20
    y = 28
    print("GCD of", x, "and", y, ":", gcd(x,y))
    
    #lcm of number
    print("LCM of 12 and 15:", lcm(12,15))
    
main()
    
