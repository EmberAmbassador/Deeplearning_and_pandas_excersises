# Oschegow Nicolaj, Bruder Luca
import traceback
# a)
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print ("You seem to be missing a file")
    #Since it was not specified whether the file should be overwritten
    #each time or should collect all tracebacks, we just chose to collect
    #all of them. Hence the parameter "a" for append.
    f = open("traceback_info.txt", "a")
    f.write(traceback.format_exc())
    f.close()

# b)
try:
    x = float(input('Enter a number:'))
except ValueError:
    print("The input was not of the right type")
try:
    y = float(input('Enter a number:'))
except ValueError:
    print("The input was not of the right type")
    
try:
    print(y, '/', x, '=', y/x)
except ZeroDivisionError:
    print("You just tried to divide by zero")
except NameError:
    print("You left one or more of the two inputs blank")

# c)
def sum_pair(L):
    sum_pair_list = []
    try:
        for i in range(len(L)):
            try:
                sum_pair_list.append(L[i]+L[i+1])
            except IndexError:
                print("You just tried to access an index which is out of range of the given list")
            except TypeError:
                print("Some elements in the given pair were of the wrong type.")
    except TypeError:
        print("The input has the wrong type")
    print('Pairwise sum:', sum_pair_list)
sum_pair([10, 5, 76, 12, 3, 9])
sum_pair([10, 5, '7', 12, 3, 9])
sum_pair(7.9)
