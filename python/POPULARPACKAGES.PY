import json

import numpy as np

a = np.zeros(10) #CREATES ARRAY OF N NUMBER OF ZEROS
print(a)

b = np.full((2,10), 0.7) #CREATES A 2D MATRIX OF 2,10 WITH VALUE OF 7
print(b)

c = np.linspace(0,25,7) #DIVIDES VALUES BETWEEN 0 AND 25 INTO 7 EQUAL PARTS
print(c)

print(type(c))

import pandas as pd

a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})

print(a) # displays the output in a very systematic format
print(a.describe()) #describe() function in pandas that will give the count, frequency, top values and frequency among other values

b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })

print(b.sort_values(by="Numbers")) # provide a sorted table 

b = b.assign(new_values = b['Numbers']*3) # assign() function takes the values present inside the table, performs an operation over them and creates a new variable called new_values that is then added to the table
print(b)

# import nltk

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# # Print statement 1
# print(word_tokenize(text)) # word_tokenize(). This takes this text and produces the first part of the output in which the words are ‘tokenized’ or simply separated by a whitespace.
# # Print statement 2
# print(nltk.tokenize.sent_tokenize(text)) #sent_tokenize() takes this block of text and tokenizes by ‘sentences’.


# stopwords = stopwords.words("english")
# new_text = []
# for i in text.split():
#     if i not in stopwords:
#         new_text.append(i)

# # Print statement 3
# print(new_text)


