import string

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

def isdigit(arg):
    if any (i for i in arg) in str(string.digits):
        print(str(string.digits))
        return True
        
    else:
        return False

