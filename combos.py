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

    combos = []

    # horizontal iteration
    
    for x in range(len(a)): # iterate through the entire grid
        for y in range(len(a[x]) - consec): # iterate through the 10 list items - 8 iterations   8 2 22  then  2 22 97 etc
            for z in range(consec): # iterate through 3 numbs at a time
                print(z)
                current_product *= a[x][y+z] # + z for third iterator [0][0] = 8  [0][1] = 2  to get the next number in the third loop
                print(current_product)
               
                
            if current_product > max_of_consecutive_numbers:
                max_of_consecutive_numbers = current_product
            current_product = 1

        print(max_of_consecutive_numbers)
        print("end of horizontal traversal")

        max_of_consecutive_numbers = max_of_consecutive_numbers
        # count how many times "iterating across" appears

        print("num of times iterating across appears")
        #print(len(combos))


findNumCombos(a, 3)