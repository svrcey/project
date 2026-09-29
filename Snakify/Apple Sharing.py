#N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
#The program reads the numbers N and K. It should print the two answers for the questions above.

n = int(input("How many students are there? "))
k = int(input("How many apples are there? "))

a1 = k // n
a2 = k % n

print("1. Each student gets", a1, "apples.")
print("2. There will be", a2, "left in the basket.")