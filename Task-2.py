
# 1.	Flatten the nested list [[1, 2], [3, 4], [5, 6]] into a single list.
l1=[[1,2],[3,4],[5,6,7]]  
l2=[]
for i in l1:
      l2.extend(i)
print(l2) 

# 2.	From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.

list =[[2, 5], [7, 9], [12, 15]]
l2=[]
for i in list:
      l2.extend(i)
for j in l2:
     if j%2==0:
          print(j)

# 3.	Create a list of squares for numbers from 1 to 20.
l1=[1,2,3,4,5,6,7]
l2=[]
for i in l1:
    l2.append(i*i)
print(l2)

# 4.	Print prime numbers between 10 to 20 using list comprehension?
ct=0
for i in range(10,20):
    for j in range(2,i):
        if i%j==0:
            ct+=1
            break
        else:
          ct=0
    if ct<1:
        print(i,"prime")

#       or

ct=0    
l1=[i for i in range(10,20) if all(i%j!=0 for j in range(2,i))]
print(l1)




# 6.	Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method.
x="HElloWorlD"
a=""
for i in x:
    if ord(i)>=65 and ord(i)<=90:
        y=ord(i)+32
        a+=chr(y)
    else:
        z=ord(i)-32
        a+=chr(z)
print(a)


# 7.	Write a list comprehension to print only the word 'python' from the list. 
s=[ 'python' ,'java' , 'c++' , 'developer' ]
x=[i for i in s if i=="python"]
print(x)



