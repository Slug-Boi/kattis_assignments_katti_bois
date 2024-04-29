import random

N = 10 # Length of starting array 0 < N <= 100_000
O = 10 # Amount of operations 0 < O <= 1_000_000

def CreateStartingArray():
    startingArray = []
    for _ in range(N):
        startingArray.append(str(random.randint(0,99))) # Add numbers between 0 - 99 both inclusive
    
    return startingArray

def CreateOperation():
    operationTypes = ["M", "S", "U"]
    operation = []
    operation.append(random.choice(operationTypes)) # Add the operation
    
    # Create update
    if operation[0] == "U":
        operation.append(str(random.randint(0, N-1))) # Add the index of the update
        operation.append(str(random.randint(0, 99))) # Add the updated value
        return operation 
    
    # Create Max and Sum 
    # Add the first index. Since first index is strictly less than the
    # second it has to be N-1 so the other can still be N
    operation.append(str(random.randint(0, N-1))) 
    # Add second index. Since this is strictly greater than the first
    # it will be between first index + 1 and N
    operation.append(str(random.randint(int(operation[1])+1, N)))
    return operation


if __name__ == "__main__":
    # Create input file
    with open("input.in", "w") as file:
        file.write(f"{N} {O}\n")
        file.write(" ".join(CreateStartingArray()) + "\n")
        for _ in range(O):
            file.write(" ".join(CreateOperation()) + "\n")