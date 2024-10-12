#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

def selection_sort(numbers) -> list:
    sorted_list = []
    
    for j in range(len(numbers) - 1):
        minimum = numbers[j]
        for i in range(1, len(numbers)):
            if numbers[i] < minimum:
                minimum = numbers[i] 
        numbers.pop(numbers.index(minimum))   
        sorted_list.append(minimum)
        print(sorted_list)
    return sorted_list

print(selection_sort([5,4,3,2,1]))
                