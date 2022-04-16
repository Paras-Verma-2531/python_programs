import re


def vowels(char):

    if char in ['a','e','i','o','u','A','E','I','O','U']:
        return char
name="hello how are you"
vow=list(filter(vowels,name))
print(vow)        