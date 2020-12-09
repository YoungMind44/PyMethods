import string

#The first argument is the delimiter
#example: join(';' , 'Hello' , 'World')
        #Output --> Hello;Wolrd
def join(*arg):
    sentence = ""
    for i in range(len(arg)):
        limiter = arg[0]
        sentence += arg[i]
        #sentence += limiter
        if i == len(arg) - 1:
            break
        sentence += limiter
    return sentence

#Function that checks if a string contains digits, returns True in that case and false if not
#Input: "43562"
#Output: True
def isdigit(arg):
    if any (i for i in arg) in str(string.digits):
        print(str(string.digits))
        return True
        
    else:
        return False

#function that sum up the numbers of a list
#input: [3, 4, 1]
#output: 8
def sum(arg):
    result = 0
    for i in arg:
        if type(i) == int or float:
            result += i
        else:
            print("Sorry, Invalid input.")
            
    return result

#function that returns the lenght of a string, a list or a tuple
#input: [1, 2, 'a'] or (1,2,3) or 'Hello'
def lenght(arg):
    count = 0
    for _ in arg:
        count += 1

    return count
#print(lenght((1,2,3)))

#The bubble sort algorithm is used in the both function maximum and minimum defined below
def bubble_sort(num_list):
    for _ in range(len(num_list)):
        for j in range(len(num_list) - 1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

#the maximum and minimum functions return respectively the maximum and minimum value of a list of numbers
def maximum(arg):
    if type(arg) == list:
        bubble_sort(arg)
        return arg[len(arg) - 1]

    else:
        raise TypeError


def minimum(arg):
    if type(arg) == list:
        bubble_sort(arg)
        #The smallest number is the first element of the sorted list
        return arg[0]
    
    else:
        raise TypeError

"""
test = [1,3,4]
print(maximum(test))
print(minimum(test))
"""




