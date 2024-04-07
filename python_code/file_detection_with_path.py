#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

import os

file_path = "/python_code/file.txt"
if os.path.exists(file_path):
    print("The file exists")
    if os.path.isfile(file_path):
        print("The file is a file")
    elif os.path.isdir(file_path):
        print("The file is a directory")
    else:
        print("But, The file is not a file")
else:
    print("The file does not exist")
    
    
try:
    # This line opens and closes the file. 
    with open(file_path, 'r+') as opened_file:
    # opened_file = open(file_path, 'a')
        opened_file.write("\nThis is the end of the file.\n")
    
except FileNotFoundError as err:
    print(err)
finally:
    print("The file is closed? ", opened_file.closed) 
    

