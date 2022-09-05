#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a program to print yourself introduction

# In[1]:


def personal_details():
    name, age = "Shankarraj", 23
    address = "Erode, Tamilnadu, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
 
personal_details()


# ## 2.Write a program to perform the following operations:
# - Addition
# - Subtraction
# - Multiplication
# - Division
# - Modulus
# - Exponent

# In[2]:


5num1=int(input("Enter a first value: "))
num2=int(input("Enter a second value: "))

#Addition

add=num1+num2
print("The Addition of two numbers {} and {} is {}".format(num1,num2,add))

#Subtraction

sub=num1-num2
print("The Subtraction of two numbers {} and {} is {}".format(num1,num2,sub))

#Multiplication

mul=num1*num2
print("The Multiplication of two numbers {} and {} is {}".format(num1,num2,mul))

#Division

div=num1/num2
print("The Division of two numbers {} and {} is {}".format(num1,num2,div))


#Modulus

mod=num1%num2
print("The Modulus of two numbers {} and {} is {}".format(num1,num2,mod))

#Exponent

exp=num1**num2
print("The Exponent of two numbers {} and {} is {}".format(num1,num2,exp))


# ##  3.write a program to swap two numbers

# In[3]:


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# ## 4. write a program to swap two numbers without using third variable

# In[4]:


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

x, y = y, x
print("x =", x)
print("y =", y)


# ## 5. Write a program to compute simple Interest

# In[5]:


p=int(input('The principal is: '))
t=int(input('The time period is: '))
r=int(input('The rate of interest is: '))

si = (p * t * r)/100

print('The Simple Interest is', si)


# ## 6. wrtie a program to find the average of five numbers by user input

# In[6]:


print("Enter the Value of n: ")
n = int(input())
print("Enter " +str(n)+ " Numbers: ")
nums = []
for i in range(n):
    nums.insert(i, int(input()))

sum = 0
for i in range(n):
    sum = sum+nums[i]

avg = sum/n
print("\nAverage = ", avg)


# ## 7. write a program to calculate the discriminant of a quadratic equation

# In[7]:


import cmath

a = int(input())
b = int(input())
c = int(input())

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# ## 8. write a program to calculate the areas of the following shapes:
# - Rectangle
# - Square
# - Trinangle
# - Circle

# In[9]:


# Python Program to find the area of triangle

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# In[10]:


# Python Program to find the area of Sqaure

s=float(input("Enter side of square"))
area=s*s
print("Area of square=",'%.2f'%area)


# In[11]:


# Python Program to find the area of Rectangle
 
w = float(input('Please Enter the Width of a Rectangle: '))
h = float(input('Please Enter the Height of a Rectangle: '))
 
# calculate the area
Area = w * h
 
print("\n Area of a Rectangle is: %.2f" %Area)


# In[12]:


# Python Program to find the area of Circle

PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
circumference = 2 * PI * radius

print(" Area Of a Circle = %.2f" %area)
print(" Circumference Of a Circle = %.2f" %circumference)


# ## 9. write a program to calculate the net salary of an employee whose basic salary is entered by the user , DA is 5% of basic salary , HRA is 7% of basic salary and PF is 3% of basic salary.

# In[13]:


name= str(input("Enter name of employee:"))
basic=float(input("Enter Basic Salary :"))
da=float(basic*0.03)
hra=float(basic*0.07)
pf=float((basic+da)*0.03)
netpay=float(basic+da+hra)

print(" NAME OF EMPLOYEE : ",name)

print(" NET SALARY PAY : ",netpay)


# ## 10.write a program to calculate the power of a number

# In[14]:


base = int(input("Enter the base value :"))
exponent = int(input("Enter the exponent value :"))

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("power = " + str(result))


# ## 11.write a program to get the python version you are using.

# In[15]:


import platform

print(platform.python_version())


# In[16]:


import sys
print(sys.version)


# In[ ]:




