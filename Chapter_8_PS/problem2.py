# Celsius to Fahrenheit
# C  / 5 = F - 32 / 9
# C = 5 * (F - 32) / 9

def f_to_c(f):
    # c = 5 * (f - 32) / 9
    # return c
    return 5 * (f - 32) / 9
    
f = int(input("Enter temperature in F: "))
# print(f_to_c(f))
c = f_to_c(f)
print(f"{round(c,2)} Degree C")