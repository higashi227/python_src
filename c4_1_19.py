#デフォルト引数を上書きする
def menu(entree='beef',drink='cola',dessert='ice'):
    print('entree=',entree)
    print('drink=',drink)
    print('dessert=',dessert)
    
menu(entree='chicken',drink='wine')#入力して上書きする