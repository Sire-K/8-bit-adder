from full_adder import operation
from full_adder import bool_operation
from inputs import assignment
from inputs import t_assignment

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
    sum = 0
    adder = adder_Operation()
    carry_var_zero = None
    for i in range(8):
        if i == 0:
            A, B, C = assignment()  
            sum_var_zero, carry_var_zero = adder.first(A, B, C) 
            sum = (sum * 10) + int(sum_var_zero)
        elif i == 1:
            A, B, C = t_assignment(carry_var_zero)                                               
            sum_var_one, carry_var_one = adder.second(A, B, carry_var_zero)      
            sum = (sum * 10) + int(sum_var_one)
        elif i == 2:
            A, B, C = t_assignment(carry_var_one)                                               
            sum_var_two, carry_var_two = adder.third(A, B, carry_var_one)        
            sum = (sum * 10) + int(sum_var_two)
        elif i == 3:
            A, B, C = t_assignment(carry_var_two)                                               
            sum_var_three, carry_var_three = adder.fourth(A, B, carry_var_two)  
            sum = (sum * 10) + int(sum_var_three)
        elif i == 4:
            A, B, C = t_assignment(carry_var_three)                                               
            sum_var_four, carry_var_four = adder.fifth(A, B, carry_var_three)    
            sum = (sum * 10) + int(sum_var_four)
        elif i == 5:
            A, B, C = t_assignment(carry_var_four)                                               
            sum_var_five, carry_var_five = adder.sixth(A, B, carry_var_four)     
            sum = (sum * 10) + int(sum_var_five)
        elif i == 6:
            A, B, C = t_assignment(carry_var_five)                                               
            sum_var_six, carry_var_six = adder.seventh(A, B, carry_var_five)     
            sum = (sum * 10) + int(sum_var_six)
        elif i == 7:
            A, B, C = t_assignment(carry_var_six)                                               
            sum_var_seven, carry_var_seven = adder.eighth(A, B, carry_var_six)   
            sum = (sum * 10) + int(sum_var_seven)

    decimal_equivalent = int(str(sum), 2)
    final_carry = int(carry_var_seven)
    print(f"Sum: {sum}")
    print(f"Sum(decimal): {decimal_equivalent}")
    print(f"Final Carry: {final_carry}")
