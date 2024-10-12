#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

class Time:
    """Time abstract data type (ADT) definition"""
    
    def __init__(self, hour, minute, second):
        """ Initialize hour, minute, and second """
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def military_watch(self):
        print("Military Clock---> %.2d: %.2d: %.2d" %(self.hour, self.minute, self.second))
        
    def standard_watch(self):
        meridian = "AM"
        if self.hour > 12:
            meridian = "PM"
        if (self.hour == 0 or self.hour == 12):
            self.hour = 12
        else:
            self.hour = self.hour % 12
        print("Standard Clock---> %2d: %2d: %2d %s" %(self.hour, self.minute, self.second, meridian))
    
    def __str__(self):
        """ Built in function used to print selected class data."""
        return f"{self.hour}:{self.minute}:{self.second}" 
        

