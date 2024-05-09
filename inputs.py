def inputs_to_bool(A, B, C):
    A = bool(A)                     #Sets A as True if 1 and False if 0
    B = bool(B)                     #Sets B as True if 1 and False if 0
    C = bool(C)                     #Sets C as True if 1 and False if 0
    return A, B, C

def assignment():
    while True:
        A = input("Value of A[0 - 1]: ")
        if not A.isdigit() or len(A) != 1:      #If A is a char and if A is input as nn+[double+ digit],
            continue                            #the loop continues, else it moves and checks if, 
        A = int(A)                              #it's a valid digit, i.e. 1 or 0.
        if A == 1 or A == 0:
            break

    while True:
        B = input("Value of B[0 - 1]: ")
        if not B.isdigit() or len(B) != 1:      #If B is a char and if B is input as nn+[double+ digit],
            continue                            #the loop continues, else it moves and checks if,
        B = int(B)                              #it's a valid digit, i.e. 1 or 0.
        if B == 1 or B == 0:
            break

    while True:
        C = input("Value of C[0 - 1]: ")
        if not C.isdigit() or len(C) != 1:      #If B is a char and if B is input as nn+[double+ digit],
            continue                            #the loop continues, else it moves and checks if,
        C = int(C)                              #it's a valid digit, i.e. 1 or 0.
        if C == 1 or C == 0:
            break

    A, B, C = inputs_to_bool(A, B, C)           #Sets inputs A, B, C as True or False.
    return A, B, C                              #True if 1 & False if 0.

def t_assignment(C):
    while True:
        A = input("Value of A[0 - 1]: ")
        if not A.isdigit() or len(A) != 1:      #If A is a char and if A is input as nn+[double+ digit],
            continue                            #the loop continues, else it moves and checks if, 
        A = int(A)                              #it's a valid digit, i.e. 1 or 0.
        if A == 1 or A == 0:
            break

    while True:
        B = input("Value of B[0 - 1]: ")
        if not B.isdigit() or len(B) != 1:      #If B is a char and if B is input as nn+[double+ digit],
            continue                            #the loop continues, else it moves and checks if,
        B = int(B)                              #it's a valid digit, i.e. 1 or 0.
        if B == 1 or B == 0:
            break
    
    Carry = C
    A, B, Carry = inputs_to_bool(A, B, Carry)
    return A, B, Carry

if __name__ == "__main__":
    assignment()
