from numpy import *

a = array([
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
    [81, 49, 99, 40, 17, 81, 18, 57, 60, 87],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
    [22, 31, 16, 71, 51, 67, 65, 89, 41, 92],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38], 
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63], 
    [24, 55, 58, 5, 66, 73, 99, 36, 97, 27],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45]]
    )
m = reshape(a,(10,10))
print(m)

def findNumCombos(a, consec):

    max_of_consecutive_numbers = 0 
    
    current_product = 1

    consec = 3

    times_end_of_row_reached = []

    times_end_of_consecutive_nums_reached = []

    # horizontal iteration
    
    for x in range(len(a)): # iterate through the entire grid
        for y in range(len(a[x]) - consec): # iterate through the 10 list items - 8 iterations   8 2 22  then  2 22 97 etc
            county = y
            times_end_of_consecutive_nums_reached.append(county)
            for z in range(consec): 
                print(z)
                current_product *= a[x][y+z] # + z for third iterator [0][0] = 8  [0][1] = 2  to get the next number in the third loop
                print(current_product)
                 
            if current_product > max_of_consecutive_numbers:
                max_of_consecutive_numbers = current_product
            current_product = 1

        print(max_of_consecutive_numbers)
        print("end of horizontal traversal")
        count = "end of horizontal traversal"
        times_end_of_row_reached.append(count)

        max_of_consecutive_numbers = max_of_consecutive_numbers
       

        print("num of times end of the row is reached")
        print(len(times_end_of_row_reached))
        print("number of times end of consecutive numbers reached")
        print(len(times_end_of_consecutive_nums_reached))

        num_combos = len(times_end_of_row_reached) + len(times_end_of_consecutive_nums_reached)
        
        print("Number of combinations for horizontal traversal:")
        print(num_combos)

        print("Number of combinations for all four directions = num_combos * 4")
        print(num_combos * 4)

        


findNumCombos(a, 3)