#!/usr/bin/env python3

"""

Node: sub_coord

Description: This node subscribes to the robot’s position and velocity (using the custom message) and prints the
distance of the robot from the target and the robot’s average speed

author: Enrico Piacenti  enricopiacenti96@gmail.com

"""

from enrico_second_assignment.msg import odom_custom_msg
import rospy
import os
import sys
import math

#istanciating global variables 
speed =0
avr_vel =0
distance=0
count =0

def subscriber(data):

    global speed
    global count
    global avr_vel
    global distance

    current_x = data.x
    current_y = data.y
    pos_x = rospy.get_param("/des_pos_x")
    pos_y = rospy.get_param("/des_pos_y")
    distance= math.sqrt(((pos_x - current_x)**2)+((pos_y - current_y)**2))

    x_speed = data.vel_x
    y_speed = data.vel_y

    curr_speed= math.sqrt((x_speed**2)+(y_speed**2))

    if count<5:

        speed=speed+curr_speed
        count +=1

    elif count==5:

        count=0
        speed /= 5
        avr_vel=speed
        speed=0


def tachimeter():
        
        while True:
            print(f"Distance of robot to the goal: {distance : .3f}")
            print(f'Average speed : {avr_vel: .3f}')
            rate.sleep()
	    


if __name__ == "__main__":

    try:
        # Writing log messages
        rospy.logwarn("sub_coord started")

        # Initializes a rospy node
        rospy.init_node('sub_coord')

        
        rospy.wait_for_message("robot_informations", odom_custom_msg)
        rate = rospy.Rate(rospy.get_param("/print_per_second"))
        rospy.Subscriber("robot_informations", odom_custom_msg, subscriber)
        tachimeter()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
