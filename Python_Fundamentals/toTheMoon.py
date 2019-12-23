# toTheMoon Function in Python
# Neil Denning

def toTheMoon(num):
    a = 1
    b = 0
    valSum = 2
    for num in range (0, num-1, 1):
        b = a + a
        a = b
        valSum += b
    return valSum

results = toTheMoon(8)
print(results)

