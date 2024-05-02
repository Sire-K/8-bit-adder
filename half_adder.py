#Though this file isn't used in the main 8 bit adder file, I created this for the sake of just being here.
from inputs import assignment

def logic(A, B, C):

    if C == True:                                    #Sets C as False
        C = False
    add = (A ^ B)                                    #XOR GATE: A XOR B
    C = (A * B)                                      #AND GATE: A AND B            

    add, C = bool_operation(add, C)

def bool_operation(add, C):
    add = bool(add)                                  #Sets add as True if 1 and False if 0
    C = bool(C)
    return add, C                                    #Sets C as True if 1 and False if 0

if __name__ == "__main__":
    A, B, C = assignment()
    logic(A, B, C)

