'''
Title     : Tuples
Subdomain : Data Types
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
numbers=raw_input().strip().split()
ar=[]
for i in range(0,len(numbers)):
   ar.append(int(numbers[i]))
t=tuple(ar)
print hash(t)
