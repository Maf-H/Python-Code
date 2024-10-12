#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
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
