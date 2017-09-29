from typing import Callable
from .check_util import *

import re


def compute_diff(arg1: float, arg2: float):
    return abs(arg1 - arg2)


def compute_value_by_ratio_and_range(ratio: float, val_range: tuple) -> float:
    check_value(ratio, is_ratio)
    check_value(val_range, is_range)
    return compute_diff(*val_range) * ratio + val_range[0]


def compute_ratio_by_value_and_range(value: float, val_range: tuple) -> float:
    check_value(val_range, is_range)
    check_value(value, make_in_specific_range(val_range))
    return (value - val_range[0]) / compute_diff(*val_range)


def make_in_specific_range(val_range):
    def in_specific_range(value: float) -> bool:
        return in_range(value, val_range)
    return in_specific_range


def try_to_map(func: Callable, value):
    if is_iterable(value):
        return type(value)(map(func, value))
    else:
        return func(value)


def search_indication_to_set_float_value(key_name: str, text: str):
    return re.compile(
        r'(?<={}=)[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'.format(key_name)
    ).search(text)


def ret_just_do_func(func, *params):
    def just_do_func():
        return func(*params)
    return just_do_func


def try_to_call_func_with_log(log, func: Callable, *params):
    if not hasattr(log, 'copy_by'):
        raise TypeError

    just_do = ret_just_do_func(func, *params)
    # noinspection PyBroadException
    try:
        ret = just_do()
    except:
        return log

    log.copy_by(ret)
    return ret
