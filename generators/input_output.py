# Tool for creating inputs and outputs for kattis problems
#
# Requirements:
#  - A generator that can create valid inputs
#  - A valid solition to the problem
# 
# A second solution can be given to cross reference with the first solution to ensure the outputs match
# 
# Usage:
#   python3 input_output.py <generator run command> <solution run command> [other_solution run command] 

import os
import filecmp
from sys import argv

if len(argv) >= 4:
    generator  = argv[1]
    solution1 = argv[2]
    solution2 = argv[3]
elif len(argv) == 3:
    generator = argv[1]
    solution1 = argv[2]
    solution2 = ""
else:
    print("Not enough arguments!")
    quit()

num_solutions = 10

os.system("mkdir inputs")
os.system("mkdir answers")
print("Generating inputs and outputs...")
for i in range(1, num_solutions+1):
    print("Generating inputs and outputs for round:", i)
    os.system(f"{generator} > {i}.in")
    os.system(f"{solution1} < {i}.in > sol1[{i}].ans")
    if solution2:
        os.system(f"{solution2} < {i}.in > sol2[{i}].ans")
        if not filecmp.cmp(f"sol1[{i}].ans", f"sol2[{i}].ans"):
            print("Error in output", i)
            break
    os.system(f"mv {i}.in inputs/{i}.in")
    os.system(f"mv sol1[{i}].ans answers/{i}.ans")
print("Done!")