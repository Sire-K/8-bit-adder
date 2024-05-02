from full_adder import operation
from full_adder import bool_operation
from inputs import assignment

class adder_Operation:
    def first(self, A, B, C):  
        out_one, out_two = operation(A, B, C) 
        sum_result, Carry_result = bool_operation(out_one, out_two)  
        sum_var_zero = sum_result
        carry_var_zero = Carry_result
        return sum_var_zero, carry_var_zero

    def second(self, A, B, carry_var_zero):
        out_one, out_two = operation(A, B, carry_var_zero)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_one = sum_result
        carry_var_one = carry_result  
        return sum_var_one, carry_var_one

    def third(self, A, B, carry_var_one):
        out_one, out_two = operation(A, B, carry_var_one)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_two = sum_result
        carry_var_two = carry_result  
        return sum_var_two, carry_var_two
    
    def fourth(self, A, B, carry_var_two):
        out_one, out_two = operation(A, B, carry_var_two)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_three = sum_result
        carry_var_three = carry_result  
        return sum_var_three, carry_var_three
    
    def fifth(self, A, B, carry_var_three):
        out_one, out_two = operation(A, B, carry_var_three)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_four = sum_result
        carry_var_four = carry_result  
        return sum_var_four, carry_var_four
    
    def sixth(self, A, B, carry_var_four):
        out_one, out_two = operation(A, B, carry_var_four)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_five = sum_result
        carry_var_five = carry_result  
        return sum_var_five, carry_var_five
    
    def seventh(self, A, B, carry_var_five):
        out_one, out_two = operation(A, B, carry_var_five)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_six = sum_result
        carry_var_six = carry_result  
        return sum_var_six, carry_var_six
    
    def eighth(self, A, B, carry_var_six):
        out_one, out_two = operation(A, B, carry_var_six)  
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_seven = sum_result
        carry_var_seven = carry_result  
        return sum_var_seven, carry_var_seven
    
if __name__ == "__main__":
    adder = adder_Operation()
    carry_var_zero = None
    for i in range(8):
        if i == 0:
            A, B, C = assignment()  
            sum_var_zero, carry_var_zero = adder.first(A, B, C) 
            print(f"Sum[{i}]: {sum_var_zero}, Carry[{i}]: {carry_var_zero}")
        elif i == 1:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_one, carry_var_one = adder.second(A, B, carry_var_zero)      #Instead of C, carry_var_zero is used.
            print(f"Sum[{i}]: {sum_var_one}, Carry[{i}]: {carry_var_one}")
        elif i == 2:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_two, carry_var_two = adder.third(A, B, carry_var_one)        #Instead of C, carry_var_one is used.
            print(f"Sum[{i}]: {sum_var_two}, Carry[{i}]: {carry_var_two}")
        elif i == 3:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_three, carry_var_three = adder.fourth(A, B, carry_var_two)   #Instead of C, carry_var_two is used.
            print(f"Sum[{i}]: {sum_var_three}, Carry[{i}]: {carry_var_three}")
        elif i == 4:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_four, carry_var_four = adder.fifth(A, B, carry_var_three)    #Instead of C, carry_var_three is used.
            print(f"Sum[{i}]: {sum_var_four}, Carry[{i}]: {carry_var_four}")
        elif i == 5:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_five, carry_var_five = adder.sixth(A, B, carry_var_four)     #Instead of C, carry_var_four is used.
            print(f"Sum[{i}]: {sum_var_five}, Carry[{i}]: {carry_var_five}")
        elif i == 6:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_six, carry_var_six = adder.seventh(A, B, carry_var_five)     #Instead of C, carry_var_five is used.
            print(f"Sum[{i}]: {sum_var_six}, Carry[{i}]: {carry_var_six}")
        elif i == 7:
            A, B, C = assignment()                                               #The program doesn't considers C here.
            sum_var_seven, carry_var_seven = adder.eighth(A, B, carry_var_six)   #Instead of C, carry_var_six is used.
            print(f"Sum[{i}]: {sum_var_seven}, Carry[{i}]: {carry_var_seven}")
