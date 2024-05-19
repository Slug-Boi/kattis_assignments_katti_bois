import random
from sys import argv

# Set the size of the input with permanent values:

# Set the size of the input with arguments:
args = argv
if len(args) > 1:
    N = int(argv[1])
    O = int(argv[2])
else:
    N = 7  # Length of starting array 0 < N <= 100_000
    O = 3  # Amount of operations 0 < O <= 1_000_000


def CreateStartingArray():
    startingArray = []
    for _ in range(N):
        # Add numbers between 0 - 99 both inclusive
        startingArray.append(str(random.randint(0, 99)))

    return startingArray


def CreateOperation():
    operationTypes = ["M", "S", "U"]
    operation = []
    operation.append(random.choice(operationTypes))  # Add the operation

    # Create update
    if operation[0] == "U":
        # Add the index of the update
        operation.append(str(random.randint(0, N-1)))
        operation.append(str(random.randint(0, 99)))  # Add the updated value
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
    # with open("input.in", "w") as file:
    #     file.write(f"{N} {O}\n")
    #     file.write(" ".join(CreateStartingArray()) + "\n")
    #     for _ in range(O):
    #         file.write(" ".join(CreateOperation()) + "\n")
    print(f"{N} {O}")
    print(" ".join(CreateStartingArray()))
    for _ in range(O):
        print(" ".join(CreateOperation()))

