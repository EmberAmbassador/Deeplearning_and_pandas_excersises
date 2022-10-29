#Exercise 3
#a) The expression causes an error since it tries to concatenate
#   a string and an integer. This is not possible without conversion.
#   A possible solution would be to convert the integer to a string.
#   'I have eaten ' + str(25) + ' peas.'

#b) The first one ('temp') is a string and the second one (temp)
#   is a variable.
#   The type of an expression expr can be check with the
#   command type(expr).

#c
import datetime

username = input("Your name: ")
print("Hello %s. Your name has %d characters." % (username, len(username)))
yob = int(input("Your year of birth: "))
age = datetime.datetime.now().year - yob
print("You seem to be about %d years old" % age)

#   This script can not always calculate the users age correctly
#   since we are not given the birthmonth. For someone who has
#   been born in 2000 the script will always calculate an age of 20,
#   where in reality the person would be 20 if he was born
#   before November and 19 if he was born in december. 
