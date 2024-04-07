#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

class Time:
    """Time abstract data type (ADT) definition"""
    public = "Public Attribute"
    __private = "Prinate Atribute"
    def __init__(self, hour = 0, minute = 0, second = 0):
        """ Initialize hour, minute, and second """
        self._hour = hour
        self._minute = minute
        self._second = second
    
    def set_time(self, hour, minute, second):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_second(second)
        
    def set_hour(self, hour):
        if (0 <= hour < 24):
            self._hour = hour
        else:
            raise ValueError ("Invalid hour: %2d" %hour)
        
    def set_minute(self, minute):
        if (0 <= minute < 60):
            self._minute = minute
        else:
            raise ValueError ("Invalid minute: %2d" %minute)
    
    def set_second(self, second):
        if (0 <= second < 60):
            self._second = second
        else:
            raise ValueError ("Invalid second: %2d" %second)
        
    def get_hour(self):
        return self._hour 
    
    def get_minute(self):
        return self._minute
    
    def get_second(self):
        return self._second 
    
    def military_watch(self):
        """" Prints time in military format"""  
        print("Military Clock---> %.2d: %.2d: %.2d" %(self._hour, self._minute, self._second))
        
    def standard_watch(self):
        """" Prints time in standard format"""

        meridian = "AM"
        if self._hour > 12:
            meridian = "PM"
            self._hour = self._hour % 12
            
        if (self._hour == 0 or self._hour == 12):
            self._hour = 12
            
        print("Standard Clock---> %.2d: %.2d: %.2d %s" %(self._hour, self._minute, self._second, meridian))
    
    def __str__(self):
        """ Built in function used to print selected class data.
            This function must return only String
        """
        return f"{self._hour}:{self._minute}:{self._second}" 
        

