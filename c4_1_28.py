#位置引数のタプル化
def say_something(word,*args):
    print('ねこ=',word)
    for arg in args:
        print(arg)
        
say_something('パンチ','hey','oi')