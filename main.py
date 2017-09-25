from my_util import *


def main():
    result = search_indication_to_set_float_value('max', 'max=4')
    if result:
        print(result.group(0))

if __name__ == '__main__':
    main()
