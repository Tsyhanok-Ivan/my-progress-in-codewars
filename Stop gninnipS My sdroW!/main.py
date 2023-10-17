# Python 3.11
# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    _sentence = sentence.split(" ")
    for i in range(len(_sentence)):
        if len(_sentence[i]) >= 5:
            _sentence[i] = _sentence[i][::-1]
    return " ".join(_sentence)
  
