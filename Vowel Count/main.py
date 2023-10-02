# Python 3.11
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    total_vowels = 0
    for i in sentence:
        total_vowels += 1 if vowels.count(i) == 1 else 0
    return total_vowels
