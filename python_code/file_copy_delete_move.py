#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu
import os
import shutil


source = 'copy_2.txt'
copy_destination = 'file.txt'
move_destination = 'move_2.txt'
delete_file = 'copy.txt'

try:
    if os.path.exists(source):
        # Deletes the file
        os.remove(delete_file)
        # Uses to copy file from source to destination
        shutil.copy2(source, copy_destination)
        if os.path.exists(move_destination):
            print("The destination file is already there.")
        else:
            # Uses to move file or folder from source to destination
            os.replace('copy_2.txt', copy_destination)
except FileNotFoundError as err:
    print(err)
