#lambda関数を使わない場合
l = ['Mon','tue','Wed','Thu','Fri','sat','Sun']

def change_words(words,func):
    for word in words:
        print(func(word))
        
def sample_func(word):
    return word.capitalize()

change_words(l,sample_func)

#lambda関数を使用したとき
l=['Mon','tue','Wed','Thu','Fri','sat','Sun']

def change_word(words,func):
    for word in words:
        print(func(word))
        
sample_func=lambda word: word.capitalize()

change_word(l,sample_func)