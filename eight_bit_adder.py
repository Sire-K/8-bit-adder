#Rs. 4500 [$33.66], Total price to make this adder component.                                 

from full_adder import operation, bool_operation
from inputs import assignment, t_assignment

class adder_Operation:
    def first(self, A, B, C):                                                       # Takes the iniitial first values form user.
        out_one, out_two = operation(A, B, C)                                       # Performs full adder operation
        sum_result, Carry_result = bool_operation(out_one, out_two)                 # Converts the results into bool.
        sum_var_zero = sum_result
        carry_var_zero = Carry_result
        return sum_var_zero, carry_var_zero                                         # returns the first sum and carry

    def second(self, A, B, carry_var_zero):                                         # Takes two value for the second adder from user
        out_one, out_two = operation(A, B, carry_var_zero)                          # while, the first adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_one = sum_result
        carry_var_one = carry_result  
        return sum_var_one, carry_var_one

    def third(self, A, B, carry_var_one):                                           # Takes two value for the third adder from user
        out_one, out_two = operation(A, B, carry_var_one)                           # while, the second adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_two = sum_result
        carry_var_two = carry_result  
        return sum_var_two, carry_var_two
    
    def fourth(self, A, B, carry_var_two):                                          # Takes two value for the fourth adder from user
        out_one, out_two = operation(A, B, carry_var_two)                           # while, the third adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_three = sum_result
        carry_var_three = carry_result  
        return sum_var_three, carry_var_three
    
    def fifth(self, A, B, carry_var_three):                                         # Takes two value for the fifth adder from user
        out_one, out_two = operation(A, B, carry_var_three)                         # while, the fourth adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_four = sum_result
        carry_var_four = carry_result  
        return sum_var_four, carry_var_four
    
    def sixth(self, A, B, carry_var_four):                                          # Takes two value for the sixth adder from user
        out_one, out_two = operation(A, B, carry_var_four)                          # while, the fifth adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_five = sum_result
        carry_var_five = carry_result  
        return sum_var_five, carry_var_five
    
    def seventh(self, A, B, carry_var_five):                                        # Takes two value for the seventh adder from user
        out_one, out_two = operation(A, B, carry_var_five)                          # while, the sixth adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_six = sum_result
        carry_var_six = carry_result  
        return sum_var_six, carry_var_six
    
    def eighth(self, A, B, carry_var_six):                                           # Takes two value for the eighth adder from user
        out_one, out_two = operation(A, B, carry_var_six)                            # while, the seventh adder passses the carry var.
        sum_result, carry_result = bool_operation(out_one, out_two)  
        sum_var_seven = sum_result
        carry_var_seven = carry_result  
        return sum_var_seven, carry_var_seven
    
if __name__ == "__main__":
    sum = 0
    n = 1                                                                            # I have used an n here to distinguish leds that
    adder = adder_Operation()                                                        # will light up when the sum is performed.
    carry_var_zero = None                                                   
    for i in range(8):
        if i == 0:
            A, B, C = assignment()                                                   # The zeroth led will light up depending on, 
            sum_var_zero, carry_var_zero = adder.first(A, B, C)                      # what the sum is, off if 0 and on if 1.
            sum = int(sum_var_zero) * n
        elif i == 1:
            A, B, C = t_assignment(carry_var_zero)                                   # The first led will light up depending on,     
            sum_var_one, carry_var_one = adder.second(A, B, carry_var_zero)          # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_one) * n)
        elif i == 2:
            A, B, C = t_assignment(carry_var_one)                                    # The second led will light up depending on,            
            sum_var_two, carry_var_two = adder.third(A, B, carry_var_one)            # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_two) * n)
        elif i == 3:
            A, B, C = t_assignment(carry_var_two)                                    # The third led will light up depending on,            
            sum_var_three, carry_var_three = adder.fourth(A, B, carry_var_two)       # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_three) * n)
        elif i == 4:
            A, B, C = t_assignment(carry_var_three)                                  # The fourth led will light up depending on,              
            sum_var_four, carry_var_four = adder.fifth(A, B, carry_var_three)        # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_four) * n)
        elif i == 5:
            A, B, C = t_assignment(carry_var_four)                                   # The fifth led will light up depending on,             
            sum_var_five, carry_var_five = adder.sixth(A, B, carry_var_four)         # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_five) * n)
        elif i == 6:
            A, B, C = t_assignment(carry_var_five)                                   # The sixth led will light up depending on,              
            sum_var_six, carry_var_six = adder.seventh(A, B, carry_var_five)         # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_six) * n)
        elif i == 7:
            A, B, C = t_assignment(carry_var_six)                                    # The seven led will light up depending on,            
            sum_var_seven, carry_var_seven = adder.eighth(A, B, carry_var_six)       # what the sum is, off if 0 and on if 1.
            sum = sum + (int(sum_var_six) * n)
            sum = sum + (int(sum_var_seven) * n)
        
        n = n * 10

    decimal_equivalent = int(str(sum), 2)                                            # Calculates the decimal equivalent of bianry sum.
    final_carry = int(carry_var_seven)                                               # Final Carry [carry_var_seven]
    print(f"Sum: {sum}")                                                             # Prints the binay sum.
    print(f"Sum(decimal): {decimal_equivalent}")                                     # Prints the decimal equibvalent sum.
    print(f"Final Carry: {final_carry}")                                             # Prints the final Carry
