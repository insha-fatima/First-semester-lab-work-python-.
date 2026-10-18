# sum the numbers
x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
z = x + y
print("sum of the numbers = ", z)

#variables and its type
a = 45
b = 9.9
c = "my name is insha"
d = [1,2,3,4,5]
e = {"fruit":"banana","colour":"yellow","quantity":7}
print("value = ",a, type(a))
print("value = ",b, type(b))
print("value = ",c, type(c))
print("value = ",d, type(d))
print("value = ",e, type(e))

#string into integer
x = "7890"
y = int(x)
print(y)

#use of AND OR NOT
marks = int(input("Mark: "))
attendance = int(input("Attendance: "))
print(marks > 33 and attendance > 75)
print(marks > 33 or attendance > 7)
print(not marks > 33)


#check the values
a = input("write a name of fruit:")
b = "i" in a
print(b)

x = [20,25,30,35,40]
y = int(input("write a number:"))
z = y in x
print(z)

# use of assignment operators
num1 = 20
num1 += 5 
print("result1 = ", num1)
num2 = 14
num2 -= 4
print("result2 = ", num2)
num3 = 19
num3 /= 3
print("result3 = ", num3)
num4 = 50
num4 **= 2
print("result = ", num4)


# use of comparision operators
num1 = 34
num2 = 6
result = num1 > num2
print("result = ", result)

a = 14
b = 19
c = a < b
print("result = ", c)

x = 19
y = 5
z = x >= y
print("result = ", z)

u = 28
v = 9
x = u <= v
print("result = ", x)

i = 32
j = 40
k = i != j
print("result = ", k)

l = 50
m = 40
n = l == m
print("result = ", n)


    



