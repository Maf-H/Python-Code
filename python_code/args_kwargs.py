#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

def delivery_address(*args, **kwargs):
    for name in args:
        print(name, end=' ')
    print()
    for address in kwargs.values():
        print(address, end=' ')


delivery_address('Mesfin', 'Haftu', 'Teshome',
                 country='Ethiopia',
                 city='Addis Ababa',
                 subcity='Yeka.')
