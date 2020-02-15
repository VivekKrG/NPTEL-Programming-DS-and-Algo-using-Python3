def merge(A,B): #Merge A[ 0: len(A)] and B[ 0 : len(B) ]
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0) #Current postion in A,B
    while i+j < m+n: #i+j is number of elements merged so far
        if i==m:
            C.append(B[j])
            j=j+1

        elif j==n:
            C.append(A[i])
            i=i+1

        elif A[i] <= B[j]:
            C.append(A[i])
            i=i+1

        elif A[i] > B[j]:
            C.append(B[j])
            j=j+1

    return (C)
def mergesort(A, left, right): #sort the slice A[left: right]
    if right -left <=1:
        return ( A[left:right] ) # Base case
    if right -left >1: # Recursive call
        mid= (left+right)//2
        l=mergesort(A,left,mid)
        r=mergesort(A,mid,right)
        return (merge(l,r))
'''
>>> l=[12,23,78,45,89,36,21,45,63,2,5,6,25,125]
>>> mergesort(l,0,len(l))
[2, 5, 6, 12, 21, 23, 25, 36, 45, 45, 63, 78, 89, 125]
>>>
'''  
def union(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0) #Current postion in A,B
    while i+j < m+n: # i+j is number of elements checked so far
        if i==m:
            C.append(B[j])
            j=j+1

        elif j==n:
            C.append(A[i])
            i=i+1

        elif A[i] < B[j]:
            C.append(A[i])
            i=i+1

        elif A[i] > B[j]:
            C.append(B[j])
            j=j+1

        elif A[i]==B[j]:
            j=j+1
            C.append(A[i])
            i=i+1       
    return (C)

def intersection(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0) #Current postion in A,B
    while i+j < m+n:
        if A[i]<B[j]:
            i=i+1
        elif B[j]<A[i]:
            j=j+1
        elif A[i]==B[j]:
            j=j+1
            C.append(A[i])
            i=i+1
    return (C)
def quicksort(A,l,r):
    if r-l<=1:
        return ()
    p1=l+1
    for p2 in range(l+1,r):
        if A[p2]<=A[l]:
            ( A[p1], A[p2] )=( A[p2], A[p1] )
            p1=p1+1
    # Move pivote into place/ b/w p1 and p2
    ( A[l],A[p1-1] )=( A[p1-1],A[l] )
    quicksort(A,l,p1-1)
    quicksort(A,p1,r)    
        












        
