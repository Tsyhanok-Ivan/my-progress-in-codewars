# Python 3.11 
# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    number = ''
    for i in list(str(num)):
        number += str(int(i) ** 2)
    return int(number)
  
