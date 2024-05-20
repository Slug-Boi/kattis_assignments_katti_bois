import random
# random.seed(100) # For testing purposes


def find_bin_len():
    light = int(input())
    if light == 1:
        print("? flip", flush=True)
        input()
    print("? left", flush=True)

    # Length of the binary number to be inserted in the train (if required)
    bin_len = 25

    for _ in range(bin_len-1):
        light = int(input())
        if light == 1:
            print("? flip", flush=True)
            input()
        print("? left", flush=True)
    light = int(input())
    if light == 0:
        print("? flip", flush=True)
        input()
        print("? right", flush=True)
    else:
        print("? right", flush=True)

    count = 1
    while True:
        light = int(input())
        if count == bin_len-1:
            return count+1, light, False
        if light != 1:
            count += 1
        else:
            if count < bin_len:
                return count, light, True
            else:
                return count+1, light, False
        print("? right", flush=True)


def insert(bin_num, light):

    cur = light

    # Insert number into train
    for i in range(len(bin_num)):
        if i != 0:
            cur = int(input())
        if str(cur) != bin_num[i]:
            print("? flip", flush=True)
            cur = int(input())
        print("? left", flush=True)

    return cur


def solver(bin_num):

    train_len = 0

    window = []

    while True:
        cur = input()
        train_len += 1
        if len(window) < len(bin_num):
            window.append(cur)
        else:
            window.pop(0)
            window.append(cur)

        if "".join(window) == bin_num:
            return train_len
        print("? left")


def findRandom():

    # Generate the random number
    num = random.randint(0, 1)

    # Return the generated number
    return str(num)


solved = False

# Get a small chunk of the train to hash random binary number on
trip = find_bin_len()
bin_len = trip[0]
light = trip[1]
solved = trip[2]

if not solved:

    # Create random hashed binary number with a certain length
    bin_num = ""
    for _ in range(bin_len):
        bin_num += findRandom()

    bin_num = bin_num[::-1]

    print("? right", flush=True)
    temp = input()

    if temp == bin_num[0]:
        print("? flip", flush=True)
        light = int(input())

    print("? left", flush=True)
    light = int(input())

    # Insert bin number in train
    light = insert(bin_num, light)

    # Run solver until train length is determined
    train_len = solver(bin_num)
else:
    train_len = bin_len


print("!", train_len, flush=True)
