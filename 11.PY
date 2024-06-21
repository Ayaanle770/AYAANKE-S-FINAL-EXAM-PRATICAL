def sum_of_odds(n):
    sum_odds = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  
            sum_odds += i
    return sum_odds


print(sum_of_odds(5))   
print(sum_of_odds(10)) 
print(sum_of_odds(100)) 
