n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} X {11 - i} = {n * (11 -i)}")

'''
    1   10      => 1 + 10 = 11
    2   9       => 2 + 9 = 11
    3   8       => 3 + 8 = 11
    4   7       => 4 + 7 = 11
    5   6       => 5 + 6 = 11
    6   5       => 6 + 5 = 11
    7   4       => 7 + 4 = 11
    8   3       => 8 + 3 = 11
    9   2       => 9 + 2 = 11
    10  1       => 10 + 1 = 11
'''