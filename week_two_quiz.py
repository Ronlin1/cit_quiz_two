"""
WEEK TWO QUIZ AS AT 05 MARCH 2020 ___PYTHON-BLOCKCHAIN-AWS-CIT-CLASS 2021___
"""
# WELCOME SCREEN
print('------------------------- WEEK TWO QUIZ --------------------------')

# TODO: QUIZ ANSWERS
# Global variable --->End of question separator in the ---- terminal ----
end_of_answer = '------------------------------------------------------------------'

# 1 --> Identified, created and re-fixed a few errors.

# 2 --> UNICODE? Converting a sting to unicode -UTF8
"""
   Unicode is a universal character encoding standard that assigns a code to every 
   character and symbol in every language in the world.
   
   The difference between ASCII and Unicode is that ASCII represents lowercase letters (a-z),
   uppercase letters (A-Z), digits (0–9) and symbols such as punctuation marks while Unicode 
   represents letters of English, Arabic, Greek etc.... 
   
   UTF-8 is the most widely used way to represent Unicode text in web pages
   UTF-8 is a Unicode Transformation Format that uses 8-bit blocks to represent
   a character and is essential for software localization.
"""

# In Python 3 and higher, all strings are already in unicode, however, we can deode every letter
# Using functions ord() and chr()

my_string = "Hello World!"
print(f'My String: {my_string}')
my_string_decoded = []
for letter in my_string:
    my_string_decoded.append((ord(letter)))

print(f'My String decoded: {my_string_decoded}')
# Note : Unicode characters include space, comma, punctuations etc...
# To convert back , we use chr()

my_string_encoded_again = []
for i in my_string_decoded:
    my_string_encoded_again.append(chr(i))
print(f'Encoded: {my_string_encoded_again}')
print('So we know H=72, e=101, l=108 and so on ... ')
print(end_of_answer)

print("\U0001F606")
print("\N{grinning face}")

# EMOJI CHALLENGE
# importing emoji module
import emoji

# simple emoji print-outs
print(emoji.emojize("Here we gat :grinning_face_with_big_eyes: and :winking_face_with_tongue: and :zipper-mouth_face:"))

# without import -> Use of \N and {} specifies Unicode
print("\N{cherry blossom}")
print("\N{slightly smiling face}")
print("\N{winking face}")

# We can use shortcodes too
print("\U0001f600 , \U0001F606 , \U0001F923, \U0001F601, \U0001F609, \U0001F60B, \U0001F60D, \U0001F680")

print(end_of_answer)
print(emoji.emojize("Yeah I think Python is :thumbs_up: and my favourite emoji is :nerd_face:"))
