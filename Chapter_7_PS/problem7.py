'''
  *
 ***
***** for n = 3
'''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="") # 2 * i - 1 (if i = 1, 2 * 1 - 1 = 1) # odd number series
    print("")