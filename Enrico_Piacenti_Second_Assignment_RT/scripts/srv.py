#!/usr/bin/env python3

"""

Node: srv

Description: This function prints the number of goals reached and cancelled

author: Enrico Piacenti  enricopiacenti96@gmail.com

"""

import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os
import sys

#instanciating global variables
target_completed =0, 
not_target_achieved = 0
seq =1 


def serv_sub(data):
    if data.status.status == 2:
        global not_target_achieved
        not_target_achieved += 1
    
    elif data.status.status == 3:
        global target_completed
        target_completed += 1
        

def service(request):
    global not_target_achieved , target_completed , seq
    print(f"Sequence: {seq}\n Number of unfulfilled tasks: {not_target_achieved}\n Number of reached goal: {target_completed}")
    seq += 1
    return EmptyResponse()


if __name__ == "__main__":
    try:
        # Writing log messages
        rospy.logwarn("Service has begun")
        # Initializes a rospy node
        rospy.init_node('srv')

        rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, serv_sub)
        rospy.Service('reach_cancel_ints', Empty, service)

        # Keeps the communucation with the ROS network open
        rospy.spin()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
