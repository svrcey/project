#A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.


print("Enter the first timestamp:")
h1 = int(input("Hours: "))
m1 = int(input("Minutes: "))
s1 = int(input("Seconds: "))

print("Now enter the second timestamp:")
h2 = int(input("Hours: "))
m2 = int(input("Minutes: "))
s2 = int(input("Seconds: "))

first = h1 * 3600 + m1 * 60 + s1
second = h2 * 3600 + m2 * 60 + s2

print("There is", second - first, "second(s) between the two timestamps.")