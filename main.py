from my_util import *


def main():
    result = search_indication_to_set_float_value('max', 'max=4')
    if result:
        print(result.group(0))

    val_range = (-5., 10.)
    ratio = compute_ratio_by_value_and_range(value=1., val_range=val_range)
    print(ratio)
    value = compute_value_by_ratio_and_range(ratio=ratio, val_range=val_range)
    print(value)

if __name__ == '__main__':
    main()
