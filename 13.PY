

def sum_of_even(n):
    sum_even = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # Check if i is even
            sum_even += i
    return sum_even

# Test cases
print(sum_of_even(5))  
print(sum_of_even(10))   
print(sum_of_even(100))  
