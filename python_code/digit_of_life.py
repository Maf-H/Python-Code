#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

birth_date = '21051985' # input("Enter birthdate using format 'Year Month Date' using number:")

while len(birth_date) != 1:
    digit_of_life = 0
    for i in range (len(birth_date)):
        digit_of_life += int(birth_date[i])
        print(digit_of_life)
    birth_date = str(digit_of_life)

print("Your  digit_of_life is: ", birth_date)

