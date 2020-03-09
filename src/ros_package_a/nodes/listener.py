#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from ros_package_a.utils import util_1


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    

if __name__ == '__main__':

    # test calling the imported util
    util_1()

    # normal rs stuff
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()
