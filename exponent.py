print(2**3)

def raiseToPower(base_num, power_num):
    return pow(base_num, power_num)

print(raiseToPower(3,2))

def raiseToPower2(base_num, power_num):
    result = 1
    for index in range(power_num):
        result *= base_num
    return result
    
base_num = float(input("Please type in the base number. "))
power_num = int(input("Please type in the power you want to raise the base number to. "))
print(raiseToPower2(base_num, power_num))