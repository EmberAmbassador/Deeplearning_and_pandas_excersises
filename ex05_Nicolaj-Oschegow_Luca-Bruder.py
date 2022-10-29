# Oschegow Nicolaj, Bruder Luca

#Converting to an integer right before converting to a float might
#ignore important decimals.
X = float(input('Quantity of enzyme X:'))

#Since we value precision and the input is not necessarlily of type
#integer we should not convert to integer, but rather keep
#the float type.mro
Y = float(input('Quantity of enzyme Y:'))

#Same as in the first line of code, it is not a good idea
#to convert the input to an integer before converting it to
#a float again, since it might lose important decimals.
Z = float(input('Quantity of enzyme Z:'))

#Our margin of error is supposed to be 10^-4, thus the epsilon is smaller
#than we need it to be.
epsilon = 1E-4

#Since we to not know which of the two enzymes X and Y is bigger
#we can not just take the difference. We need to take the absolute
#difference because we might get false positives and or negatives otherwise.
#Furthermore we need the difference between the two to be LESS than our
#margin of error to pass the test.
#Lastly the statement is missing a ':'

#While this does correctly calculate the difference in most cases, it does
#struggle with precision due to python. While this would for example correctly
#print out "Danger!" for the X and Y values 0.0001 and 0.0002 it does the
#opposite for the number pair 1.0001 and 1.0002. The outcome should be the
#same, yet it is not.
if abs(X-Y) < epsilon:
    print('Test passed.')

#Another missing ':'
else:
    print('DANGER!')
