#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from ros_package_a.some_ros_util import util_1
from package_foo.foo import foo_calls_bar


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


if __name__ == '__main__':

    # test calling methods from the package
    util_1()
    foo_calls_bar()

    # normal ros stuff
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()
