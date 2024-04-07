#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

import os

print(os.getcwd())


class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)

        except OSError as err:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir(".."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
