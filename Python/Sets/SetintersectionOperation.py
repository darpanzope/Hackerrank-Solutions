'''
Title     : Set .intersection() Operation
Subdomain : Sets
Domain    : Python
Author    : Darpan Zope
Created   : 
Problem   : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
'''
e = int(input())
eng = set(map(int,input().split()))
f = int(input())
fre = set(map(int,input().split()))
print(len(eng & fre))
