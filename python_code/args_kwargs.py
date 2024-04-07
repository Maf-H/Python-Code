#  Copyright (c) 27-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

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
