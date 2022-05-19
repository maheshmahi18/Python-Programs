# using Temporary variable
a=int(input("enter a:"))
b=int(input("enter b:"))
t=a
a=b
b=t
print("using Temporary variable")
print('a:',a)
print('b:',b)

#using without Temporary variable
a=int(input("enter a:"))
b=int(input("enter b:"))
(a,b)=(b,a)
print("using without Temporary variable")
print('a:',a)
print('b:',b)
