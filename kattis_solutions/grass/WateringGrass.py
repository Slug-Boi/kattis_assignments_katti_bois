import sys
from math import sqrt

n = 0
l = 0
    
def findMin(sprinklers):
    hi = 0
    minS = 0
    
    n = len(sprinklers)
    i = 0
    for count in range(l):
        currentMax = -1
        while i < n and sprinklers[i][0] <= hi:
            if currentMax < sprinklers[i][1]:
                currentMax = sprinklers[i][1]
            i += 1
        minS += 1
        hi = currentMax
        if hi >= l:
            return minS
        elif hi == -1:
            return -1


for line in sys.stdin:
    if n > 0:
        n -= 1
        x,r = map(int,line.split())
        if (r+r) > w: # If not then that sprinkler diameter won't help cover anything
            r = sqrt(r**2 - w**2/4) # Calculate the distance from the center of the sprinkler to the edge of the sprinkler
            
            # List of tuples (range, left side, right side)
            # first element is range on left side
            ls = x-r
            
            # second element is range on right side
            rs = x+r
            
            # apppend the ring into the list with the range first so that it can be sorted by that
            # the left and right side are added so the range for each side is there
            # sprinklerInfo.append(((rang),(ls),(rs)))
            sprinklerInfo.append((ls,rs))
            
        if n == 0:
            print(findMin(sorted(sprinklerInfo)))
            
    else: 
        sprinklerInfo = [] # for reseting when it starts again with a new case
        n,l,w = map(int,line.split())
    
        
        
