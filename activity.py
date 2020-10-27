#CS 325 Fall 2020
#Brittany Sundberg
#HW 4


#merge sort functions to use later, modified to look at the start time of of the activities stored (since our activities will be an array of arrays
def Merge(array_a, array_b):
    """modification of Merge to look at the inner index of the array of arrays, and to sort in descending order"""
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a][1] > array_b[index_b][1]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    """sorts an array using the divide and conquer strategy"""
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)



infile = open('act.txt', 'r')
set = 1
while(True):
    activities = []
    test = infile.readline()
    if test == "" or test == "\n":
        break
    num_activities = int(test)
    for i in range(num_activities):
        line = infile.readline().strip()
        act = line.split()
        for k in range(0, len(act)):
            act[k] = int(act[k])
        activities.append(act)
    activities = merge_sort(activities)
    selected_activities = []
    selected_activities.append(activities[0][0])
    m = 0
    for i in range(2, len(activities)):
        if activities[i][2] <= activities[m][1]:
            selected_activities.append(activities[i][0])
            m = i
    act_out = ""
    for l in range(len(selected_activities)-1, -1, -1):
        act_out += str(selected_activities[l])
        if l != 0:
            act_out += " "
    print("Set", set)
    print("Number of Activities Selected =", len(selected_activities))
    print("Activities:", act_out)
    set += 1