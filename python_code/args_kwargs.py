#  Copyright (c) 27-06/04/2024, 16:48.
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
