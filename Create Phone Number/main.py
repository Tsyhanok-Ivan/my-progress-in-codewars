# Python 3.11
# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    n = "".join(map(str, n))
    return "({}) {}-{}".format(n[0:3], n[3:6], n[6:10])
  
