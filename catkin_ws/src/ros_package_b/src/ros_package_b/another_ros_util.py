from ros_package_a.msg import MessageA
from package_foo.foo import foo_calls_util_1


def util_2():
    print("util_2")
    foo_calls_util_1()
    MessageA()
