#!/usr/bin/env python

import rospy

from package_foo.foo import foo_calls_bar

from ros_package_a.msg import MessageA
from ros_package_a.some_ros_util import util_1


if __name__ == '__main__':
    rospy.init_node('package_a_node')

    util_1()
    foo_calls_bar()

    MessageA()
