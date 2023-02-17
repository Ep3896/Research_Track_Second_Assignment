#! /usr/bin/env python3

"""

Node: custom_msg

Description: this node has the aim of publishing a desired type of ROS message

author: Enrico Piacenti  enricopiacenti96@gmail.com

"""

import rospy
from nav_msgs.msg import Odometry
from enrico_second_assignment.msg import odom_custom_msg
import os
import sys


def pub(info):
    publishes_robot_info = rospy.Publisher('robot_informations', odom_custom_msg, queue_size=5)
    custom_message = odom_custom_msg()
    custom_message.x = info.pose.pose.position.x
    custom_message.y = info.pose.pose.position.y
    custom_message.vel_x = info.twist.twist.linear.x
    custom_message.vel_y = info.twist.twist.linear.y
    publishes_robot_info.publish(custom_message)


if __name__ == '__main__':
    try:
        rospy.init_node('custom_msg')    
        rospy.Subscriber("/odom", Odometry, pub)
        rospy.spin()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)


