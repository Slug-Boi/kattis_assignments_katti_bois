
# This code is very heavily inspired by the following links
# https://www.geeksforgeeks.org/iterative-segment-tree-range-maximum-query-with-node-update/?ref=lbp
# https://www.geeksforgeeks.org/segment-tree-efficient-implementation/


# limit for array size  
N,O = map(int,input().split())
# Max size of tree 
# Nodes in the tree are a tuple of (sum, max)
# Leaf nodes are just a value (sum, max) = (value, value)
sumtree = [0] * (2 * N)
maxtree = [0] * (2 * N)
# function to build the tree  
def buildMaxTree(arr):
    # insert leaf nodes in tree  
    for i in range(n):  
        maxtree[n + i] = arr[i]
      
    # build the tree by calculating parents  
    for i in range(n - 1, 0, -1):  
        maxtree[i] = max(maxtree[2 * i], maxtree[2 * i + 1])

def buildSumTree(arr): 
  
    # insert leaf nodes in tree  
    for i in range(n):  
        sumtree[n + i] = arr[i]
      
    # build the tree by calculating parents  
    for i in range(n - 1, 0, -1):  
        sumtree[i] = sumtree[i << 1] + sumtree[i << 1 | 1]
        
# function to update a tree node  
def updateSumTreeNode(p, value):  
      
    # set value at position p  
    p = p + n  
    sumtree[p] = value
      
    # move upward and update parents p functions as i here 
    while p > 1: 
        # XOR operation gets the other node. So if we update the left node XOR will get the right node and vice versa
        sumtree[p >> 1] = sumtree[p] + sumtree[p ^ 1]
        p >>= 1  

def updateMaxTreeNode(p, value):
    # set value at position p  
    p = p + n  
    maxtree[p] = value
      
    # move upward and update parents p functions as i here 
    while p > 1: 
        # XOR operation gets the other node. So if we update the left node XOR will get the right node and vice versa
        maxtree[p >> 1] = max(maxtree[p], maxtree[p ^ 1])
        p >>= 1 

# function to get sum on interval [l, r)  
def sum_query(l, r):  
  
    res = 0
      
    # loop to find the sum in the range  
    l += n
    r += n
      
    while l < r: 
        
        # Could use bitwise & but python automagically translates mod 2 operations to bitwise and
        if (l % 2): 
            res += sumtree[l]
            l += 1
      
        if (r % 2): 
            r -= 1
            res += sumtree[r]
              
        l >>= 1
        r >>= 1
      
    return res

def max_query(l,r):
    
    res = 0 
      
    # loop to find the sum in the range  
    l += n
    r += n 
      
    
    while l < r: 
        
        # Could use bitwise & but python automagically translates mod 2 operations to bitwise and
        if (l % 2): 
            res = max(res,maxtree[l])  
            l += 1
      
        if (r % 2): 
            r -= 1 
            res = max(res,maxtree[r])  
              
        l >>= 1
        r >>= 1
      
    return res 

def parser(ch, n1, n2):
    match ch:
        case 'M':
            print(max_query(n1,n2))
        case 'S':
            print(sum_query(n1,n2))
        case 'U':
            updateSumTreeNode(n1,n2)
            updateMaxTreeNode(n1,n2)
           
a = list(map(int,input().split()))

# n is the size of the input array  
n = len(a)

# build tree  
buildSumTree(a)
buildMaxTree(a)

for _ in range(O):
    ch, n1, n2 = input().split()
    parser(ch, int(n1), int(n2))