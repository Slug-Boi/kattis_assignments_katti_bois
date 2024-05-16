import random

bin_len = random.randint(4, 5000)

number = random.getrandbits(bin_len)

bin_num = format(number, '0b')

print(bin_num, end="")
