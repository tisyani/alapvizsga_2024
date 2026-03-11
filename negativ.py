import random
negativok = 0

def negativ(num):
    if num < 0:
        return True
    else:
        return False
    
for i in range(100):
    if negativ(random.randint(-50, 50)) == True:
        negativok += 1

print(f"Negatív számok száma: {negativok}")