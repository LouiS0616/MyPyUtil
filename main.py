from my_util import *


class MyInt:
    def __init__(self, value=None):
        self._value = value

    def copy_by(self, value):
        self._value = value

    def __str__(self) -> str:
        return str(self._value)


def main():
    a = MyInt()
    print(try_to_call_func_with_log(a, int, '3'))
    print(a)

    print(try_to_call_func_with_log(a, int, '3.5'))
    print(a)

if __name__ == '__main__':
    main()
