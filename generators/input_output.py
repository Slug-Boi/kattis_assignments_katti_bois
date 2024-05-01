import os
import filecmp

generator  = "segment_tree.py"
solution1 = "group_sol.py"
solution2 = "group_sol.py" # Add the name of the cpp binary

num_solutions = 10

print("Generating inputs and outputs...")
for i in range(1, num_solutions+1):
    print("Generating inputs and outputs for round:", i)
    os.system(f"python3 {generator} 10 2 > {i}.in")
    os.system(f"python3 {solution1} < {i}.in > py{i}.ans")
    # vvv Uncomment when having working cpp binary vvv
    # os.system(f"./{solution2} < {i}.in > cpp{i}.ans")
    # if not filecmp.cmp(f"py{i}.ans", f"cpp{i}.ans"):
    #     print("Error in output", i)
    #     break
print("Done!")