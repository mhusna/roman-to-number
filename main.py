def to_number(roman):
    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    increments = 0
    decrements = 0
    
    for i in range(len(roman)-1):
        if (numbers[roman[i]] < numbers[roman[i+1]]):
           decrements += numbers[roman[i]]
        else:
           increments += numbers[roman[i]]
           
    increments += numbers[roman[len(roman) - 1]]
    total = increments - decrements
    
    return total

print(to_number("MCMVII"))  #1907
print(to_number("MMXI"))    #2011
print(to_number("XC"))      #90
print(to_number("MCMXC"))   #1990