#!/usr/bin/env python3
#
# Testing tool for the Going in Circles problem
#
# Usage:
#
#   python3 testing_tool.py [-s sequence] <program>
#
# The sequence must consist of characters '0' and '1' and have length at least 3.
# If no initial sequence is specified, the sample (011) is used.
#
# You can compile and run your solution as follows.
# - You may have to replace 'python3' by just 'python'.
# - On Windows, you may have to replace '/' by '\'.
#
# If you have a Java solution that you would run using
# "java MyClass", you could invoke the testing tool with:
#
#   python3 testing_tool.py java MyClass
#
# If you have a Python solution that you would run using
# "python solution.py", you could invoke the testing tool with:
#
#   python3 testing_tool.py python solution.py
#
# If you have a C++ solution stored in a file called "sol.cpp",
# you must first compile using "g++ sol.cpp -o sol" and then
# invoke the testing tool with:
#
#   python3 testing_tool.py ./sol
#
# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it
# is not guaranteed that a program that passes the testing tool
# will be accepted.


# Troublesome binary number
# 10000010001100001111000111111000110011110001000101101000101011100100110000010011011011001111111000011011011111101011000111101110111000010011110001111101101101111010101000001011100111100111100010011011000110010110100111011110111110011111011011110001100001010101100110001010110110101100011000100000110111111011111011110010001100011110111000011011011111000001111010001110110111111010101110100000010001101011110011111010100010001101010111000101100101110100101111000001100110001111010100001100010110001000101011010001100000010001000110001101011100101101101100001010001110001111011010000011101110110110011110111101101110001000000000001010111010010100111100100010111000010001110100010111101011110101000111101100101010000011001110111010110110011110010111000101000100100001011001111111101001010001100000111110001011011110111111000110000011111011110101100001010111100110001011100110111011100000010001001011000011111010101010011000011100111011111100010011101001000110001011010110000011010110001111001011111100101000010000001000111011000010001101100100000100101011011100011010110000110110001111110001111010111001010000101011001011010011001101011111101100001010011110110011110010011111001100100111100111000011110110000100000111011100001001100111011100111011001001010111010111101111000001011000101001001110011010101001110010000001101010011100001001011000100001000100100101111001011001100000000110010011111110000010010110011010100010011010000010000110110011011110010111101100010101001001110000100001001011001000010111111010000100101100001010011000001010110100100001111000011010011001110001011100010110110010111110011011011011111100110100100111100011100111101000110110111111101011011100101111110010000

#
import argparse
import subprocess
import sys
import traceback


def write(p, line):
    assert p.poll() is None, 'Program terminated early'
    print('Write: {}'.format(line), flush=True)
    p.stdin.write('{}\n'.format(line))
    p.stdin.flush()


def read(p):
    assert p.poll() is None, 'Program terminated early'
    line = p.stdout.readline().strip()
    assert line != '', 'Read empty line or closed output pipe. Make sure that your program started successfully.'
    print('Read: %s' % line, flush=True)
    return line


def wrong_answer(p, reason):
    sys.stdout.write('%s\n' % reason)
    p.kill()


parser = argparse.ArgumentParser(
    description='Testing tool for the Going in Circles problem')
parser.add_argument('-s', dest='sequence', metavar='sequence', default="011")
parser.add_argument('program', nargs='+', help='Invocation of your solution')

args = parser.parse_args()

sequence = list(args.sequence)
for c in sequence:
    assert c in '01', f'Character {c} may not appear in the input sequence.'
n = len(sequence)
assert n >= 3, f'Sequence must have length at least 3'
position = 0

queries = 0
queries_limit = 3 * n + 500

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                      universal_newlines=True) as p:
    try:
        write(p, sequence[position])

        while True:
            response = read(p)

            if response.startswith('? '):
                if queries == 50000:
                    wrong_answer(p, 'Program used too many queries, aborting')
                    break
                queries += 1
                action = response[2:]
                if action == 'right':
                    position = (position + 1) % n
                elif action == 'left':
                    position = (position - 1) % n
                elif action == 'flip':
                    sequence[position] = str(1 - int(sequence[position]))
                else:
                    wrong_answer(p, 'Program gave unrecognized action')
            elif response.startswith('! '):
                answer = response[2:]
                assert answer.isnumeric(), 'Expected final guess to be a positive integer'
                answer = int(answer)
                if answer == n:
                    assert queries <= queries_limit, 'Program printed correct solution, but used too many queries'
                    assert p.stdout.readline() == '', 'Printed extra data after finding solution'
                    assert p.wait() == 0, 'Did not exit cleanly after finishing'
                    break
                else:
                    wrong_answer(p, 'Program printed incorrect solution')
                    break
            else:
                wrong_answer(p, 'Program gave invalid response')
                break

            write(p, sequence[position])
    except:
        traceback.print_exc()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write(
            f'Used {queries} queries, limit is {queries_limit}.\nProgram exit code: {p.wait()}\n')
        sys.stdout.flush()
