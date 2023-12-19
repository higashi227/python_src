#位置引数（書く位置によって渡される場所が決まる）
def menu(entree,drink,dessert):
    print('entree=',entree)
    print('drink=',drink)
    print('dessert=',dessert)
    
menu('beef','beer','ice')

#位置引数（順番を変えてみる）
def menu(entree,drink,dessert):
    print('entree=',entree)
    print('drink=',drink)
    print('dessert=',dessert)
    
menu('beef','ice','beer')