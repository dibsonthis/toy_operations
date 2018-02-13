import os
import sys

### OVERVIEW ###

# This is a toy "assembly" like language created in Python. All you have to do is change the code below to make calculations and changes to the 16-bit "memory". Here's a quick overview:

# A single calculation works in this fashion: OPERATION OPERAND1 OPERAND2 eg. ADD 5 5

# Multiple calculations work in this fashion: OPERATION (OPERATION OPERAND1 OPERAND2)(OPERATION OPERAND1 OPERAND2) eg. ADD (MUL 5 5)(DIV 10 2) // this operation first runs through the division, then multiplication, then it adds them all together. This is equivalent to the equation (5 * 5) + (10 / 2). Multiple operations can be strung together indefinitely...it'll just get really confusing.

# Equations can be nested, meaning that anywhere an operand should exist, an operation that would produce the operand can take place. eg. ADD 10 (MUL (ADD 5 5)(DIV 12 2)). This is equivalent to 10 + ((5 + 5) * (12 / 2))

# Note that brackets are not necessary, they can be excluded. However they help to make your code more readable.

### OPERATIONS ###

# ADD (+)
# SUB (-)
# MUL (*)
# DIV (/)
# EXP (** or ^)

### STORING RESULTS OF OPERATIONS AND EQUATIONS TO MEMORY ###

# Each line should contain either a single operation or a nested equation that reduces to a single result. At the beginning of every line, a memory address should exist that would store this result.
# Eg. 0x0 ADD 5 5 (This inserts the result of 5 + 5 into 0x0)
# Eg. 0x1 ADD 0x0 (MUL 5 (DIV 10 2)) (This inserts the result of [the value of 0x0] + (5*(10/2)) )

### NON MATHEMATICAL OPERATIONS ###

# INS (Inserts a number into memory) // Eg. 0x0 INS 15 or 0x1 INS 0x0 (The address or value after INS is inserted to the address before INS)
# DEL (Deletes address value) // Eg. DEL 0x0 0x1 0x2 (Multiple address values can be deleted at once)
# SHOW MEM (Prints current state of memory)

### THE CODE ###
# The code below inserts 12 in 0x0, adds the value of 0x0 * the value of 0x0 and the value of 0x0 to the power of the value of 0x0 and inserts that into 0x1, deletes the value of 0x0 to free space, inserts the value of 0x1 to 2x1 and then prints the state of the memory

# All lines in the code are split by a newline. Go ahead and play around with it!

code = "0x0 INS 12\n0x1 ADD (MUL 0x0 0x0) (EXP 0x0 0x0)\n DEL 0x0\n2x3 INS 0x1\nSHOW MEM"

debug = True

if debug == False:
    sys.tracebacklimit=None
else:
    sys.tracebacklimit=1000

def is_address():
    try:
        if 'x' in line[index-1]:
            line[index-1] = line[index-1].split('x')
            line[index-1] = [int(x) for x in line[index-1]]
            if memory[line[index-1][0]][line[index-1][1]]:
                line[index-1] = memory[line[index-1][0]][line[index-1][1]][0]
            else:
                print('Error: Address is either empty or does not exist - Line {}, "{}"'.format(position+1,line))
                os._exit(1)

        if 'x' in line[index-2]:
            line[index-2] = line[index-2].split('x')
            line[index-2] = [int(x) for x in line[index-2]]
            if memory[line[index-2][0]][line[index-2][1]]:
                line[index-2] = memory[line[index-2][0]][line[index-2][1]][0]
            else:
                print('Error: Address is either empty or does not exist - Line {}, "{}"'.format(position+1,line))
                os._exit(1)
    except TypeError:
        pass


# Mock memory
memory = [  [ [],[],[],[] ],
            [ [],[],[],[] ],
            [ [],[],[],[] ],
            [ [],[],[],[] ]  ]

store_addresses = {}

for index, character in enumerate(code):
    if character == '(' or character == ')':
        code = code.replace(character, " ")

code = code.split('\n')
code = [x.split() for x in code]
code = [x[::-1] for x in code]

for position, line in enumerate(code):

    store_addresses[position] = []

    while len(line) > 1:

        if "x" in line[-1]:
            store_addresses[position].append(line.pop(-1))

        for index, word in enumerate(line):

            if word == 'ADD':

                is_address()

                line[index-2:index+1] = [float(line[index-1]) + float(line[index-2])]
                break

            if word == 'SUB':

                is_address()

                line[index-2:index+1] = [float(line[index-1]) - float(line[index-2])]
                break

            if word == 'MUL':

                is_address()

                line[index-2:index+1] = [float(line[index-1]) * float(line[index-2])]
                break

            if word == 'DIV':

                is_address()

                line[index-2:index+1] = [float(line[index-1]) / float(line[index-2])]
                break

            if word == 'EXP':

                is_address()

                line[index-2:index+1] = [float(line[index-1]) ** float(line[index-2])]
                break

            if word == 'DEL':
                line[index-1] = line[index-1].split('x')
                line[index-1] = [int(x) for x in line[index-1]]
                if memory[line[index-1][0]][line[index-1][1]]:
                    del memory[line[index-1][0]][line[index-1][1]][0]
                    del line[index-1]
                    break
                else:
                    print('Error: Address is either empty or does not exist - Line {}, "{}"'.format(position+1,line))
                    os._exit(1)

            if word == 'INS':

                if 'x' in line[index-1]:
                    line[index-1] = line[index-1].split('x')
                    line[index-1] = [int(x) for x in line[index-1]]
                    try:
                        line[index-1] = memory[line[index-1][0]][line[index-1][1]][0]
                    except IndexError:
                        print('Error: Address is not empty - Line {}, "{}"'.format(position+1,line))
                        os._exit(1)

                try:
                    memory[line[index+1][0]][line[index+1][1]]

                    print('Error: Address is either empty or does not exist - Line {}, "{}"'.format(position+1,line))
                    os._exit(1)

                except IndexError:
                    code[position] = [float(line[index-1])]
                    del line[index-1:index+1]
                    break

            if word == 'SHOW':
                if line[index-1] == 'MEM':
                    for i in memory:
                        print(i)
                    del line[index-1]

    result = code[position]

    for index, address in enumerate(store_addresses[position]):
        store_addresses[position][index] = address.split('x')
        store_addresses[position][index] = [int(x) for x in store_addresses[position][index]]
    for index, address in enumerate(store_addresses[position]):
        memory[address[0]][address[1]] = result
