#!/usr/bin/env python

import rospy

from package_bar.bar import bar_fn

from ros_package_a.msg import MessageA
from ros_package_a.some_ros_util import util_1

from ros_package_b.msg import MessageB


if __name__ == '__main__':
    rospy.init_node('package_b_node')

    util_1()
    bar_fn

    MessageA()
    MessageB()
