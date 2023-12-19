#キーワード引数の辞書化（forループ)
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k,v)
        
menu(entree='beef',drink='cola')