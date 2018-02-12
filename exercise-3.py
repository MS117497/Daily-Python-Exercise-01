# Michael Spagnola - Python Daily Exercise 3 - 02112018

#3 Write a program that prints out the numbers from 1 to 20.
# For multiples of three, print "usb" instead of the number and for the mulitiples of five, print "device".
# For numbers which are multiples of both three and five, print "usb device".
# Print a new line after each string or number.

for i in range(20):
    number = i + 1
    
    if((number % 3 == 0) and (number %5 == 0)):
       print 'usb device'
    elif(number % 3 == 0):
        print 'usb'
    elif(number % 5 == 0):
        print 'device'
    else:
       print number
