class my_func:
    def __call__(self):
        print('func is called')

func1 = my_func()
func1()

class stock:
    def __getattribute__(self, name: str) -> None:
        print(name, 'object is approached')

f = stock()
f.data