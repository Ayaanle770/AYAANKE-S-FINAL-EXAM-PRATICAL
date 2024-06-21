


def same_data_type(lst):
    if not lst:
        return True 

    first_type = type(lst[0])
    for item in lst[1:]:
        if type(item) != first_type:
            return False
    return True


print(same_data_type([1, 2, 3, 4, 5]))           
print(same_data_type([1.0, 2.5, 3.0, 4.5, 5.1]))  
print(same_data_type(['apple', 'banana', 'cherry']))  
print(same_data_type([1, 'apple', True]))       
print(same_data_type([]))                        
