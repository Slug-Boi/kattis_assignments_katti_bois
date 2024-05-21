import random
import sys

# if first arg == 0 then genearate the worst case scenario


def worst_case():
    start = "111111111111111111111110"
    number = random_num_gen(4975)

    full = start + number + "1"

    print(full, end="")


def random_num_gen(len):
    arr = []
    for i in range(len):
        arr.append(str(random.randint(0, 1)))

    return "".join(arr)


if len(sys.argv) > 1:
    if sys.argv[1] == "w":
        worst_case()
        exit()


bin_len = random.randint(3, 5000)

number = random_num_gen(bin_len)


print(number, end="")
