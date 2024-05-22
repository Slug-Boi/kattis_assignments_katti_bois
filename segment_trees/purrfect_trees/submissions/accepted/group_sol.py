#!/usr/bin/env python3
# This code is very heavily inspired by the following links
# https://www.geeksforgeeks.org/iterative-segment-tree-range-maximum-query-with-node-update/?ref=lbp
# https://www.geeksforgeeks.org/segment-tree-efficient-implementation/


# limit for array size  
N,O = map(int,input().split())
# Max size of tree 
# Nodes in the tree are a tuple of (sum, max)
# Leaf nodes are just a value (sum, max) = (value, value)
tree = [(0,0)] * (2 * N)
# function to build the tree  

def build(arr): 
  
    # insert leaf nodes in tree  
    for i in range(n):  
        tree[n + i] = (arr[i], arr[i])
      
    # build the tree by calculating parents  
    for i in range(n - 1, 0, -1):  
        tree[i] = (tree[i << 1][0] + tree[i << 1 | 1][0], max(tree[2 * i][1], tree[2 * i + 1][1]))
        
# function to update a tree node  
def updateTreeNode(p, value):  
      
    # set value at position p  
    p = p + n  
    tree[p] = (value,value) 
      
      
    # move upward and update parents p functions as i here 
    while p > 1: 
        # XOR operation gets the other node. So if we update the left node XOR will get the right node and vice versa
        tree[p >> 1] = (tree[p][0] + tree[p ^ 1][0], max(tree[p][1], tree[p ^ 1][1]))
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
            res += tree[l][0] 
            l += 1
      
        if (r % 2): 
            r -= 1
            res += tree[r][0]
              
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
            res = max(res,tree[l][1])  
            l += 1
      
        if (r % 2): 
            r -= 1 
            res = max(res,tree[r][1])  
              
        l >>= 1
        r >>= 1
      
    return res 

def parser(ch, n1, n2):
    if ch == 'M':
        print(max_query(n1,n2))
    elif ch == 'S':
        print(sum_query(n1,n2))
    elif ch == 'U':
        updateTreeNode(n1, n2)
 
           
a = list(map(int,input().split()))

# n is the size of the input array  
n = len(a)

# build tree  
build(a)

for _ in range(O):
    ch, n1, n2 = input().split()
    parser(ch, int(n1), int(n2))