
from random import choice
word_first = 'и'
word_second = ''
library = {}


#найдем количество симвлов файла
file = open('garri_1.txt', 'r')
g = file.read()
file.close()

#откроем файл для работы с ним
file = open('garri_1.txt', 'r')


length = int(input('Количество слов: '))

#обучение, создание словаря.

for i in range(5000):#в идеале надо поставить весь текст(variable = len(g)), но это слишком долго
    letter = file.read(1)
    
    if letter.isalpha():
        word_second += letter
        
    else:
        
        word_second = word_second.lower()
        
        if word_first in library and word_second != '':
            words = library[word_first]
            if word_second not in words:
                words.append(word_second)
                library[word_first] = words

        elif word_second != '':
            words = []
            words.append(word_second)
            library[word_first] = words

        if word_second != '':
            word_first = word_second
            word_second = ''

#создание нового текста
new_text = ''
x = 0
number_words = [i for i in range(3,16)]
for i in range(length + 1):
    if x == 0:
        length_sentence = choice(number_words)
    
    first_word = choice(list(library.keys()))
    
    if first_word not in library:
            first_word = choice(list(library.keys()))
            
    else:
        words = library[first_word]
        second_word = choice(words)
        
        if x == 0:
            new_text += first_word.title() + ' '
        elif x == length_sentence:
            new_text += first_word + '.' + ' '
            x = -1
        else:
            new_text += first_word + ' '
            
        first_word = second_word
    x += 1
    
    
file.close()
print(new_text)
        
        
