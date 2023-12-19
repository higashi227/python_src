#キーワード引数を辞書型で
def menu(**kwargs):
    print(kwargs)
    
menu(entree='beef',drink='coffee')