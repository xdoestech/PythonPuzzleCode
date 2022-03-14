'''
Created on Mar 2, 2022

@author: axyzh


if slowest + fastest < secondfastest + second fastest 
    have fastest come back everytime
    
else have slowest and third slowest go together
'''
#Problem 1
def across_bridge(people: list) -> int:
    """Finds the minimum time for 4 people to cross a bridge. 
    It is dark, and it is necessary to use a torch when crossing the bridge, 
    but they have only one torch between them. The bridge is narrow, and only two 
    people can be on it at any one time. The four people take the given amounts of
    time to cross the bridge; when two cross together they proceed at the speed
    of the slowest. The torch must be ferried back and forth across the bridge, 
    so that it is always carried when the bridge is crossed.
    @param a list of 4 positive integers representing the times of the 4 people
    @return the minimum amount of time possible for the 4 people to get across the 
bridge
    """
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # shift elements larger than key one up
        j = i-1 #starts searching at begining 
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    
    return arr

def time_to_cross(arr):
    fastest = arr[0]
    second = arr[1]
    third = arr[2]
    slowest = arr[3]
    if fastest + slowest < second + second:
        #fastest goes with everyone
        t = second+third+ slowest + 2*fastest
    if fastest + slowest > second + second:
        #third and fourth go together
        t = second+fastest+ slowest + second + second
    return t

    
people = [5,10,20,25]    
sortedSquad = insertionSort(people)     
time_to_cross(sortedSquad)
print(people)
print(time_to_cross(sortedSquad))
    
###################################################################################

