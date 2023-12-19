#位置引数とタプル化と辞書化
def menu(food,*args,**kwargs):
    print(food)
    print(args)
    print(kwargs)
    
menu('banana','apple','orage','lemon',entree='beef',drink='cola')