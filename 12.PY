

def sum_of_odds(n):
    sum_odds = 0
    for num in range(1, n + 1):
        if num % 2 != 0:
            sum_odds += num
    return sum_odds

# Test cases
print(sum_of_odds(5))    
print(sum_of_odds(10))  
print(sum_of_odds(100))  
