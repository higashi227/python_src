#位置引数のタプル化（Forループ）
def say_something(*args):
    for arg in args:
        print(arg)
        
say_something('hi!','mike','nancy')
