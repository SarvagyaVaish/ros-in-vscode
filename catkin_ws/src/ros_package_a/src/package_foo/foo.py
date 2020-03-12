from package_bar.bar import bar_fn
from ros_package_a.some_ros_util import util_1


def foo_fn():
    print("foo_fn")


def foo_calls_bar():
    print("foo_calls_bar")
    bar_fn()


def foo_calls_util_1():
    print("foo_calls_util_1")
    util_1()
