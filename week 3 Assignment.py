"""
Week 3: Assignment
Q1.
Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it.
For instance:

  >>> descending([])
  True

  >>> descending([4,4,3])
  True

  >>> descending([19,17,18,7])
  False
"""
def descending(l):
  if len(l)==0 or len(l)==1:
    return(True)
  for i in range( 1 , len(l) ):
    if l[i-1] < l[i]:
      return(False)
      break
  else:
    return(True)
    
"""
Q2.
A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of 
strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing
sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

  >>> valley([3,2,1,2,3])
  True

  >>> valley([3,2,1])
  False

  >>> valley([3,3,2,1,2])
  False
"""  
def valley(l):
  if len(l) <3:
    return (False)
  num = 0
  for i in range(1, len(l)):
    if l[i-1] == l[i]:
        return(False)
    if l[i-1] > l[i]:
      num+=1
    if l[i-1] < l[i]:
      break

  if num==0:
    return (False)

  num2=0
  
  for i in range (num+1, len(l)):
    if l[i-1] >= l[i]:
      return(False)
    num2+=1

  if num2==0:
    return (False)

  return (True)

    
"""
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.
For instance, the matrix

  1  2  3
  4  5  6 
would be represented as [[1, 2, 3], [4, 5, 6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

  1  4  
  2  5
  3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the 
transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty 
matrix.

  >>> transpose([[1,4,9]])
  [[1], [4], [9]]

  >>> transpose([[1,3,5],[2,4,6]])
  [[1, 2], [3, 4], [5, 6]]

  >>> transpose([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""
def transpose(m):
  if len(m)==0:
    return ([])
  trans=[]  
  for i in range( len(m[0]) ):
    inn=[]
    for j in range( len(m) ):
      inn.append( m[j][i] )
    trans.append(inn)
  return (trans)




"""
Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index  listname.insert(index, object)
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

Built-in Functions with List
Function	Description
all()	Return True if all elements of the list are true (or if the list is empty).
any()	Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	Return the length (the number of items) in the list.
list()	Convert an iterable (tuple, string, set, dictionary) to a list.
max()	Return the largest item in the list.
min()	Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()	Return the sum of all elements in the list.

"""











  
