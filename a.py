class  Demo:
    def __init__(self):
        self.name="blues"
    def func(self):
        print(f"这是a.py里，{self.name}写的第一行代码")

if __name__ == '__main__':

    d=Demo().func()

