from inputs import assignment

def operation(A, B, C):
    
    output_one = int(A ^ B ^ C)                                         # XOR Gate: A XOR B XOR C
    output_two = int((A & B) | (C & (A ^ B)))                           # Combinational Gate: (A AND B) OR (C and (A XOR B))
   
    output_one, output_two = bool_operation(output_one, output_two)     # Sets O1 and O2 as T or F
    
    return output_one, output_two                                       # Return the values of output_one and output_two

def bool_operation(out_one, out_two):
    out_one = bool(out_one)                                             # Sets add as True if 1 and False if 0
    out_two = bool(out_two)                                             # Sets C as True if 1 and False if 0
    return out_one, out_two
