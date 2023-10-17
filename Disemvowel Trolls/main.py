# Python 3.11
# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    for i in list("aeiouAEIOU"):
        string_ = string_.replace(i, "")
    return string_
