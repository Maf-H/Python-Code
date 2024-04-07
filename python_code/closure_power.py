#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

def closure_power(exp):
    loc = exp

    def power(bas):
        return bas ** exp
    return power


f_square = closure_power(2)
f_qube = closure_power(3)

for i in range(5):
    print(i, f_square(i), f_qube(i))
