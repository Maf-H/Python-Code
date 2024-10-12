#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

class Mouse:
    def __init__(self, name):
        self.my_name = name

    def __str__(self):
        return self.my_name


class LabMouse(Mouse):
    pass


print("Is Mouse subclass of LabMouse: ", issubclass(Mouse, LabMouse), "\nIs LabMouse subclass of Mouse: ", issubclass(LabMouse, Mouse))
# Prints "False True

mickey = Mouse('mickey')
print(mickey)  # Prints "mickey".
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".
mickey = Mouse("ውሮ")
minnie = Mouse('ጎሹ')
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".
# super().method returns nearest supper class method.
