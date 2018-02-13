# EXAMPLE
    0x0 ADD ((EXP 10 (MUL 4 (DIV (EXP 2 2) 8))) (DIV (SUB 9 4) (DIV (MUL 8 0.32) 18)))
    
The above code equates to 135.15625 and is stored in memory address 0x0 in our faux 16-bit memory


# OVERVIEW

This is a toy "assembly" like language created in Python. All you have to do is change the code below to make calculations and changes to the 16-bit "memory". Here's a quick overview:

A single calculation works in this fashion: <b>OPERATION OPERAND1 OPERAND2</b> eg. <b>ADD 5 5</b>

Multiple calculations work in this fashion: <b>OPERATION (OPERATION OPERAND1 OPERAND2)(OPERATION OPERAND1 OPERAND2)</b> eg. <b>ADD (MUL 5 5)(DIV 10 2)</b> // this operation first runs through the division, then multiplication, then it adds them all together. This is equivalent to the equation (5 * 5) + (10 / 2). Multiple operations can be strung together indefinitely...it'll just get really confusing.

Equations can be nested, meaning that anywhere an operand should exist, an operation that would produce the operand can take place. eg. <b>ADD 10 (MUL (ADD 5 5)(DIV 12 2))</b>. This is equivalent to 10 + ((5 + 5) * (12 / 2))

Note that brackets are not necessary, they can be excluded. However they help to make your code more readable.

# OPERATIONS

### ADD (+)
### SUB (-)
### MUL (*)
### DIV (/)
### EXP (** or ^)

# STORING RESULTS OF OPERATIONS AND EQUATIONS TO MEMORY

Each line should contain either a single operation or a nested equation that reduces to a single result. At the beginning of every line, a memory address should exist that would store this result.
Eg. <b>0x0 ADD 5 5</b> (This inserts the result of 5 + 5 into 0x0)
Eg. <b>0x1 ADD 0x0 (MUL 5 (DIV 10 2))</b> (This inserts the result of [the value of 0x0] + (5*(10/2)) )

# NON MATHEMATICAL OPERATIONS

INS (Inserts a number into memory) // Eg. <b>0x0 INS 15</b> or <b>0x1 INS 0x0</b> (The address or value after INS is inserted to the address before INS)
DEL (Deletes address value) // Eg. <b>DEL 0x0 0x1 0x2</b> (Multiple address values can be deleted at once)
SHOW MEM (Prints current state of memory)

# THE CODE
The code featured in the source inserts 12 in 0x0, adds the value of 0x0 * the value of 0x0 and the value of 0x0 to the power of the value of 0x0 and inserts that into 0x1, deletes the value of 0x0 to free space, inserts the value of 0x1 to 2x1 and then prints the state of the memory

### This project is solely for fun and definitely a work in progress.
