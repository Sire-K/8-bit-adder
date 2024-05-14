#Though this file isn't used in the main 8 bit adder file, I created this for the sake of just being here.
from inputs import assignment

def logic(A, B, C):

    if C == True:                                        # Sets C as False
        C = False
    add = (A ^ B)                                        # XOR GATE: A XOR B
    carry = (A * B)                                      # AND GATE: A AND B            

    add_var, carry_var = bool_operation(add, carry)
    print(f"Add: {add_var}, Carry: {carry_var}")

def bool_operation(add, carry):
    add_variable = bool(add)                             # Sets add as True if 1 and False if 0
    carry_variable = bool(carry)
    return add_variable, carry_variable                  # Sets C as True if 1 and False if 0

